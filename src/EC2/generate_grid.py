"""
generate_grid.py

monitors SQS queue for messages requesting grid generation. Orchestrates the staging of data, execution of mbgrid,
staging of output, update of orders database table, and responding to step function
"""
import boto3
import logging
import json
import time
from datetime import timezone
from datetime import datetime
import argparse
from os import path
from os import remove
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from zipfile import ZipFile, ZIP_DEFLATED
from grid_task import GridTask


def main():
    mandatory_fields = ['order_id', 'TaskToken']

    # run forever
    while True:
        # WaitTimeSeconds enables Long Polling
        messages = queue.receive_messages(WaitTimeSeconds=10)
        logger.debug(f"found {len(messages)} notifications in queue to process...")

        for message in messages:
            body = json.loads(message.body)
            try:
                required_fields_present(body, mandatory_fields)
            except Exception as e:
                err_msg = str(e)
                logger.error(err_msg)
                send_failure(task_token, error_cause=err_msg)
                message.delete()
                continue

            task_token = body['TaskToken']
            order_id = body['order_id']
            logger.info(body)
            try:
                # get order/dataset info from DynamoDB
                grid_params = get_grid_params(order_id)
                output_locations = get_output_locations(order_id)

                # prep input and execute mbgrid
                data_files = stage_data_files(output_locations)
                grid_task = GridTask(order_id, data_files, grid_params)
                grid_task.execute()
                logger.info("mbgrid execution complete")
                logger.debug(grid_task.stdout)

                logger.debug("packaging results into zip file...")
                zip_filename = zip_files(order_id, data_files)

                # upload to S3 delivery bucket
                logger.debug("uploading zip file to delivery S3 bucket...")
                s3_key = upload_file_to_s3(zip_filename)

                update_order(order_id, s3_key, status='complete')

                payload = {
                    'status': 'SUCCESS',
                    'message': 'successfully generated grid'
                }
                logger.debug("notifying step function of success...")
                send_success(task_token, payload)

                logger.debug(f'deleting message for order_id {order_id}')
                message.delete()

            except Exception as e:
                logger.error(e)
                logger.error('Failed to process message and will not retry')
                message.delete()
                update_order(order_id=order_id, output_file=None, status='FAILED')
                # notify step function
                payload = {
                    'status': 'FAILURE',
                    'message': 'failed to generate grid'
                }
                # send success so step function will continue to notify user
                send_success(task_token, payload)
                continue

            finally:
                cleanup(order_id, data_files)

        # wait before getting the next batch from the queue
        logger.debug(f"all messages processed. waiting for {SLEEP_MINUTES} minutes before checking again...")
        time.sleep(SLEEP_MINUTES*60)
    # end of infinite while loop


def stage_data_files(output_locations):
    if len(output_locations) < 1:
        raise Exception("there must be at least one data file")
    data_files = {}

    # stage CSB data
    if 'csb' in output_locations:
        csv_file = download_file_from_s3(output_locations['csb'])
        data_files['csb'] = convert_csv_to_xyz(csv_file)

    # stage MB data
    if 'multibeam' in output_locations:
        data_files['multibeam'] = download_file_from_s3(output_locations['multibeam'])

    return data_files


def get_output_locations(order_id):
    """retrieve the S3 locations for dataset outputs from DynamoDB item(s)"""
    response = table.query(
        KeyConditionExpression=
        Key('PK').eq('ORDER#' + order_id) &
        Key('SK').begins_with('DATASET')
    )
    items = response['Items']
    if len(items) < 1:
        raise Exception(f'no datasets items found for order ${order_id}')

    return {i['SK'].split('#')[1]:i['output_location'] for i in items if 'output_location' in i}


def get_grid_params(order_id):
    """retrieve the grid parameters from the order item in DynamoDB"""
    response = table.get_item(
        Key={'PK': 'ORDER#' + order_id, 'SK': 'ORDER'},
        ProjectionExpression='bbox,grid'
    )
    if 'Item' not in response:
        raise Exception(f'no order found for id ${order_id}')
    bbox = [float(i) for i in response['Item']['bbox'].split(',')]
    # Boto3 deserializes to Decimal types
    format = int(response['Item']['grid']['format'])
    resolution = int(response['Item']['grid']['resolution'])
    return {'format': format, 'resolution': resolution, 'bbox': bbox}


def required_fields_present(payload, field_list):
    for i in field_list:
        if i not in payload:
            raise Exception(f"payload is missing field {i}")
    return payload


def send_success(task_token, payload=None):
    response = sfn.send_task_success(
        taskToken=task_token,
        output=json.dumps(payload)
    )
    return response


def send_failure(task_token, error_code='', error_cause=''):
    response = sfn.send_task_failure(
        taskToken=task_token,
        error=error_code,
        cause=error_cause
    )
    return response


def download_file_from_s3(file_uri):
    """
    download file from S3 using specified key
    :param filename: S3 object key
    :return: fully-qualified file name of downloaded file
    """
    *_, bucket, filename = file_uri.split('/')
    file_path = INCOMING_DIR + filename
    logger.debug(file_path)
    path.exists(file_path)
    if path.exists(file_path):
        logger.warning(f'WARNING: file {filename} already downloaded, no action taken.')
        return file_path

    logger.debug(f'downloading file {filename}...')
    with open(file_path, 'wb') as f:
        s3.download_fileobj(bucket, filename, f)
    file_size_in_mb = round((path.getsize(file_path) / 1048576), 2)
    logger.info(f'downloaded {file_size_in_mb} MB')
    return file_path


def upload_file_to_s3(filename):
    """
    upload file to S3 using file basename as key
    :param filename: file to upload
    :return: S3 key if file was successfully uploaded, None otherwise
    """

    if not path.exists(filename):
        logger.warning(f'WARNING: file {filename} not found')
        return None

    object_name = filename.split('/')[-1]

    try:
        s3.upload_file(filename, OUTPUT_BUCKET, object_name)
    except ClientError as e:
        logger.error(e)
        return None

    file_size_in_mb = round((path.getsize(filename) / 1048576), 2)
    logger.info(f'uploaded {file_size_in_mb} MB')

    return object_name


def read_large_file(file_handler):
    for line in file_handler:
        yield line.strip()


def convert_csv_to_xyz(filename):
    """
    Convert incoming CSV file to XYZ optimized for MB-System processing.

    CSV file produced by Athena has quotes around all fields (including numeric
    ones) which mbgrid does not like.  Also strip out unnecessary attributes
    and standardize lon/lat coordinate precision to reduce file size and speed
    processing.

    :param filename: fully-qualified CSV filename downloaded from S3
    :return: fully-qualified file name of XYZ file
    """
    # file naming convention is "/path/to/file/<executionid>.csv"
    execution_id = filename.split('/')[-1].split('.')[0]
    output_filename = f'{INCOMING_DIR}{execution_id}.xyz'
    if path.exists(output_filename):
        logger.warning(f'WARNING: file {output_filename} already exists, no action taken')
        return output_filename

    output_file = open(output_filename, 'a')
    with open(filename) as file_handler:
        header = file_handler.readline()
        for line in read_large_file(file_handler):
            # pull out the first 3 values (x,y,z) and standardize precision
            values = [float(value.replace('"', '')) for value in line.split(',')[0:3]]
            # limit lon, lat precision to ~1.1m at equator
            values[0] = str(round(values[0], 5))
            values[1] = str(round(values[1], 5))
            values[2] = str(round(values[2], 1))
            output_file.write(','.join(values) + "\n")
    output_file.close()
    return output_filename


def zip_files(order_id, data_files):
    """package specific processing artifacts for delivery to user
       includes CSB CSV file and any grid files with names in format <order_id>.[asc | grd]
       TODO add README file and potential other grid format extensions"""
    zip_filename = INCOMING_DIR + order_id + '.zip'

    file_list = [ f"{INCOMING_DIR}{order_id}.{i}" for i in ['asc', 'grd']]
    if 'csb' in data_files:
        # fully-qualified filename. replace xyz file with csv version
        file_list.append(f"{data_files['csb'].split('.')[0]}.csv")
    with ZipFile(zip_filename, 'w') as zip_file:
        for file_path in file_list:
            archived_filename = file_path.split('/')[-1]
            if path.exists(file_path):
                # specify with relative path use unqualified filename in Zip
                zip_file.write(file_path, arcname=archived_filename, compress_type=ZIP_DEFLATED)

    return zip_filename


def update_order(order_id, output_file, status='complete'):
    """update the order's status in DynamoDB"""
    logger.debug("updating order status to 'complete'")

    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    output_uri = f"s3://{OUTPUT_BUCKET}/{output_file}"

    # TODO add constraint to reject update if item does not already exist
    response = table.update_item(
        Key={
            'PK': 'ORDER#' + order_id,
            'SK': 'ORDER'
        },
        UpdateExpression='SET #status = :status, last_update = :now, output_location = :uri',
        ExpressionAttributeValues={
            ':status': status,
            ':now': now,
            ':uri': output_uri
        },
        ExpressionAttributeNames={
            "#status": "status"
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise Exception("failed to update order")


def cleanup(order_id, data_files):
    print(data_files)
    removed_files = []
    # bit of a hack since a *.csv file accompanies the *.xyz but is not listed in the data_files dict
    if 'csb' in data_files:
        filename = data_files['csb'].split('.')[0] + '.csv'
        if path.exists(filename):
            logger.debug(f"removing file {filename}...")
            removed_files.append(filename)
            remove(filename)
    for i in data_files:
        filename = data_files[i]
        if path.exists(filename):
            logger.debug(f"removing file {filename}...")
            removed_files.append(filename)
            remove(filename)
    for ext in ['asc', 'datalist', 'mb-1', 'xyz', 'grd', 'grd.cmd', 'zip']:
        filename = f"{INCOMING_DIR}{order_id}.{ext}"
        if path.exists(filename):
            logger.debug(f"removing file {filename}...")
            removed_files.append(filename)
            remove(filename)
    return removed_files


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    arg_parser = argparse.ArgumentParser(
        description="""monitor AWS queue and generate grid from CSB points and/or multibeam FBT files. Notify Step function when complete"""
    )
    arg_parser.add_argument("--profile", default="default", help="AWS profile")
    args = arg_parser.parse_args()

    SLEEP_MINUTES = 1                     # wait time before checking queue again
    QUEUE_NAME = 'GridDataQueue'
    ORDERS_TABLE = 'bathy-orders'
    # INCOMING_DIR = '/Users/jcc/Downloads/'
    INCOMING_DIR = '/home/ec2-user/incoming/'
    OUTPUT_BUCKET = 'order-pickup'

    session = boto3.Session(profile_name=args.profile)
    sqs = session.resource('sqs')
    dynamodb = session.resource('dynamodb')
    s3 = session.client('s3')
    sfn = boto3.client('stepfunctions')
    queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
    table = dynamodb.Table(ORDERS_TABLE)

    main()
