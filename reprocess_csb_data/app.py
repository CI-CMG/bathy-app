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


def upload_to_s3(bucket, obj_key, data):
    with io.BytesIO() as f:
        # write CSV header
        f.write(bytes('ENTRY_DATE,H3,LON,LAT,DEPTH,TIME,PLATFORM_NAME,PROVIDER\n', 'utf-8'))

        for line in data:
            f.write(bytes(line, 'utf-8'))
        f.seek(0)
        s3_client.upload_fileobj(f, bucket, obj_key)


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
        filename = obj_key.split('/')[-1]
        bucket_name = task['s3BucketArn'].split(':')[-1]
        output_bucket_name = 'bathy-csb-data'
        logger.debug(f"Got task: process file {bucket_name}/{obj_key}")

        # dict of lists where key is H3 index for the partition, and list
        # contains each record for that partition
        partitions = {}

        obj = s3.Object(bucket_name, obj_key)
        entry_date = extract_date_from_filename(obj.key)
        # WARNING: loads entire file into memory. may not scale for really large files
        lines = obj.get()['Body'].iter_lines()
        # skip first line (assumed to be header)
        next(lines)

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
                bad_records += 1
                continue

            line_counter += 1
            # replace two fields from old format w/ new
            fields[0] = entry_date
            h3_index = h3.geo_to_h3(float(lat), float(lon), 1)
            fields[1] = h3_index

            # first record in this h3 tile
            if h3_index not in partitions.keys():
                partitions[h3_index] = []

            partitions[h3_index].append(','.join(fields) + '\n')

        # store reprocessed data in output bucket
        for h3_index in partitions:
            output_obj_key = f"{h3_index}/{filename}"
            upload_to_s3(output_bucket_name, output_obj_key, partitions[h3_index])

        if line_counter:
            result_code = 'Succeeded'
            result_string = f"{line_counter} records written across {len(partitions.keys())} partitions."
            if bad_records:
                result_string += f" {bad_records} invalid records."
            logger.info(f"file {filename}: {result_string}")

        else:
            # TODO better to raise Exception here?
            result_code = 'PermanentFailure'
            result_string = "no valid records"
            logger.warning(f"file {filename}: {result_string}")

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
