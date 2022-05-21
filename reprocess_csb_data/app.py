import json
import logging
import io
from urllib import parse
import boto3
from botocore.exceptions import ClientError
import h3

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

s3_client = boto3.client('s3')
s3 = boto3.resource('s3')

"""
designed to be called by S3 Batch. Reprocesses CSB CSV-format files as stored in 
BDP bucket (arn:aws:s3:::noaa-bathymetry-pds). Removes unneeded attributes and 
adds entry_date (derived from filename) along with h3 index. Also sets prefix
object prefix based on h3 index and copies to new bucket. Will split file if 
contents cross multiple h3 tiles.

:param event: The S3 batch event containing the ID of the CSV file to process
:param context: Context about the event.
:return: A result structure that S3 uses to interpret the result of the 
    operation. When the result code is TemporaryFailure, S3 retries the operation.
"""


def extract_date_from_filename(filename):
    # expect filename in the format: csv/2019/03/06/20190306_27a0f0710fc935ce44b83b6d539d2d44_pointData.csv
    # extract date from filename because object path (i.e. prefix) may be specific to BDP bucket
    date_str = filename.strip().split('/')[-1].split('_')[0]
    # return date in ISO8601 format
    return f'{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]}'


def valid_geocoords(lonStr, latStr):
    try:
        lon = float(lonStr)
        lat = float(latStr)
    except:
        return False
    return -180 <= lon <= 180 and -90 <= lat <= 90


def lambda_handler(event, context):
    # logger.debug(event)

    # Parse job parameters from Amazon S3 batch operations
    invocation_id = event['invocationId']
    invocation_schema_version = event['invocationSchemaVersion']

    results = []
    result_code = None
    result_string = None

    # will there ever be more than one task?
    task = event['tasks'][0]
    task_id = task['taskId']

    try:
        obj_key = parse.unquote(task['s3Key'], encoding='utf-8')
        bucket_name = task['s3BucketArn'].split(':')[-1]
        output_bucket_name = 'bathy-csb-data'
        logger.info(f"Got task: process file {bucket_name}/{obj_key}")

        # file handles for each part of the incoming file. Key is H3 index for the partition
        output_files = {}

        obj = s3.Object(bucket_name, obj_key)
        entry_date = extract_date_from_filename(obj.key)
        # WARNING: loads entire file into memory. may not scale for really large extracts
        lines = obj.get()['Body'].iter_lines()
        # skip first line (assumed to be header)
        next(lines)

        with io.BytesIO() as f:
            # write CSV header
            f.write(bytes('ENTRY_DATE,H3,LON,LAT,DEPTH,TIME,PLATFORM_NAME,PROVIDER\n', 'utf-8'))
            line_counter = 0
            bad_records = 0
            for line in lines:
                # unique_id, file_uuid, lon, lat, depth, obstime, platform_name, provider = line.decode().split(',')
                fields = line.decode().split(',')
                lon = fields[2].strip()
                lat = fields[3].strip()

                # skip any record w/ invalid lon, lat coords
                if not valid_geocoords(lon, lat):
                    logger.warning(f'bad coordinates: {lon}, {lat}')
                    bad_records = bad_records + 1
                    continue

                line_counter = line_counter + 1
                # replace two fields from old format w/ new
                fields[0] = entry_date
                h3_index = h3.geo_to_h3(float(lat), float(lon), 1)
                fields[1] = h3_index
                output_line = ','.join(fields) + '\n'
                f.write(bytes(output_line, 'utf-8'))

            f.seek(0)
            filename = obj_key.split('/')[-1]
            output_obj_key = f"{h3_index}/{filename}"
            s3_client.upload_fileobj(f, output_bucket_name, output_obj_key)

            # if h3_index in output_files.keys():
            #     # file already opened and initialized w/ header
            #     file_handle = output_files[h3_index]
            # else:
            #     file_handle = init_output_file(filename, h3_index)
            #     output_files[h3_index] = file_handle

            # file_handle.write(','.join(fields) + '\n')
            # end for each line loop
        # output file closed

        # file_content = file.get()['Body'].read().decode('utf-8')
        # lines = file_content.splitlines()
        # print(len(lines))
        # print(lines[0])
        # print(lines[1])
        # print(lines[2])
        # object = s3_client.get_object(Bucket=bucket_name, Key=obj_key)
        # counter = 0
        # for line in object['Body'].read().splitlines():
        #     decoded_line = line.decode('utf-8')
        #     print(f"{counter}: {decoded_line}")
        #     counter = counter + 1

        if line_counter > 0:
            result_code = 'Succeeded'
            # TODO
            result_string = f"{line_counter} records written across x partitions. {bad_records} invalid records."
            logger.info(f"file {obj.key}: {result_string}")
            # logger.info(f'file {obj.key}: {line_counter} records written across {len(output_files.keys())} partitions')
        else:
            # TODO better to raise Exception here?
            result_code = 'PermanentFailure'
            result_string = "no valid records"
            logger.warning(f"file {obj.key}: {result_string}")

    except ClientError as error:
        logger.error(f"ClientError: {str(error)}")

    except Exception as error:
        # Mark all other exceptions as permanent failures.
        result_code = 'PermanentFailure'
        result_string = str(error)
        logger.exception(error)

    finally:
        results.append({
            'taskId': task_id,
            'resultCode': result_code,
            'resultString': result_string
        })

    return {
        'invocationSchemaVersion': invocation_schema_version,
        'treatMissingKeysAs': 'PermanentFailure',
        'invocationId': invocation_id,
        'results': results
    }


class NoDataInFileException(Exception):
    pass


class NoOutputFileException(Exception):
    pass


class MissingPartitionKeyException(Exception):
    pass


class InvalidPartitionException(Exception):
    pass
