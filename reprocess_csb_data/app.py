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

import json
import logging
import io
import os
from urllib import parse
import boto3
from botocore.exceptions import ClientError
import h3

# TODO set logging level from env var
logger = logging.getLogger(__name__)
logger.setLevel('INFO')

s3 = boto3.resource('s3')
s3_client = s3.meta.client

# approx 607,220 km2/hexagon or 418 km/side
H3_RESOLUTION = 1

# NCPP
# OUTPUT_BUCKET_NAME = 'bathy-csb-data'

# NCIS
OUTPUT_BUCKET_NAME = 'csb-data'

OUTOUT_FILE_HEADER = 'ENTRY_DATE,H3,LON,LAT,DEPTH,TIME,PLATFORM_NAME,PROVIDER\n'
OUTPUT_DIR = '/tmp/csv'
INCOMING_DIR = '/tmp/incoming'


def extract_date_from_filename(filename):
    # expect filename in the format: 20190306_27a0f0710fc935ce44b83b6d539d2d44_pointData.csv
    date_str = filename.strip().split('_')[0]
    # return date in ISO8601 format
    return f'{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]}'


def valid_geocoords(lonStr, latStr):
    try:
        lon = float(lonStr)
        lat = float(latStr)
    except ValueError:
        return False
    return -180 <= lon <= 180 and -90 <= lat <= 90


def upload_data_to_s3(bucket, obj_key, data):
    with io.BytesIO() as f:
        # write CSV header
        f.write(bytes(OUTOUT_FILE_HEADER, 'utf-8'))

        for line in data:
            f.write(bytes(line, 'utf-8'))
        f.seek(0)
        logger.debug('storing {len(data)} records in S3 key {obj_key}...')
        bucket.upload_fileobj(f, obj_key)


def memory_based_processing(obj, filename):
    """"
    in-memory processing strategy. Faster but unable to accommodate large files
    """
    # dict of lists where key is H3 index for the partition, and list
    # contains each record for that partition
    partitions = {}

    entry_date = extract_date_from_filename(filename)
    # WARNING: loads entire file into memory. may not scale for really large files
    lines = obj.get()['Body'].iter_lines()
    # skip first line (assumed to be header)
    next(lines)

    line_counter = 0
    bad_records = 0
    for line in lines:
        # WARNING: hardcoded dependency on incoming file format
        # UNIQUE_ID,FILE_UUID,LON,LAT,DEPTH,TIME,PLATFORM_NAME,PROVIDER
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
        h3_index = h3.geo_to_h3(float(lat), float(lon), H3_RESOLUTION)
        fields[1] = h3_index

        # first record in this h3 tile
        if h3_index not in partitions.keys():
            partitions[h3_index] = []

        partitions[h3_index].append(','.join(fields) + '\n')

    # store reprocessed data in output bucket
    output_bucket = s3.Bucket(OUTPUT_BUCKET_NAME)
    for h3_index in partitions:
        output_obj_key = f"csv/{h3_index}/{filename}"
        upload_data_to_s3(output_bucket, output_obj_key, partitions[h3_index])

    return line_counter, bad_records, len(partitions.keys())


def init_output_file(filename, partition):
    os.makedirs(f'{OUTPUT_DIR}/{partition}', exist_ok=True)
    f = open(f'{OUTPUT_DIR}/{partition}/{filename}', "w")
    f.write(OUTOUT_FILE_HEADER)
    return f


def download_file_from_s3(obj):
    """
    download file from S3 using specified key
    :param obj: S3 object key
    :return: fully-qualified file name of downloaded file
    """
    os.makedirs(INCOMING_DIR, exist_ok=True)
    filename = obj.key.split('/')[-1]
    filepath = f'{INCOMING_DIR}/{filename}'
    obj.download_file(filepath)
    file_size_in_mb = round((os.path.getsize(filepath) / 1048576), 2)
    logger.debug(f'downloaded {filename} ({file_size_in_mb} MB)')
    return filepath


def upload_file_to_s3(filename):
    """
    upload file to S3
    :param filename: fully-qualified filename to upload
    :return: S3 key if file was successfully uploaded, None otherwise
    """

    if not os.path.exists(filename):
        msg = f"Unable to upload to S3: file {filename} not found"
        logger.warning(msg)
        raise Exception(msg)

    # e.g. /tmp/csv/81447ffffffffff/20220301_c693417ef6a8caeccb660b5a228af576_pointData.csv ->
    #          csv/81447ffffffffff/20220301_c693417ef6a8caeccb660b5a228af576_pointData.csv
    obj_key = '/'.join(filename.split('/')[-3:])

    try:
        s3.Object(OUTPUT_BUCKET_NAME, obj_key).upload_file(filename)
    except ClientError as e:
        logger.error(f"error uploading file to S3: {str(e)}")
        raise e

    file_size_in_mb = round((os.path.getsize(filename) / 1048576), 2)
    logger.debug(f'uploaded object {obj_key} ({file_size_in_mb} MB)')
    return obj_key


def filesystem_based_processing(obj, filename):
    """"
    file processing strategy using ephemeral disk storage. Slower but able to accommodate large files
    """
    original_file = download_file_from_s3(obj)
    line_counter = 0
    bad_records = 0
    output_files = {}
    entry_date = extract_date_from_filename(filename)

    with open(original_file) as fh:
        header = fh.readline()
        for line in read_large_file(fh):
            fields = line.split(',')
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
            h3_index = h3.geo_to_h3(float(lat), float(lon), H3_RESOLUTION)
            fields[1] = h3_index
            if h3_index not in output_files.keys():
                output_files[h3_index] = init_output_file(filename, h3_index)

            output_files[h3_index].write(','.join(fields) + '\n')

    # close all output files and upload
    for fh in output_files.values():
        fh.close()
        upload_file_to_s3(fh.name)

    return [line_counter, bad_records, len(output_files)]


def read_large_file(file_handler):
    for line in file_handler:
        yield line.strip()


# seems /tmp is not necessarily cleaned at the termination of each execution
def remove_files_from_temp_dir():
    for path, currentDirectory, files in os.walk("/tmp"):
        for file in files:
            logger.debug(f"removing {os.path.join(path, file)}...")
            os.remove(os.path.join(path, file))


def lambda_handler(event, context):
    # logger.debug(event)
    remove_files_from_temp_dir()

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
        logger.debug(f"Got task: process file {bucket_name}/{obj_key}")

        obj = s3.Object(bucket_name, obj_key)
        logger.debug(f"file {obj_key} has {obj.content_length} bytes")

        if obj.content_length < 1000000:
            # logger.debug('using memory_based_processing...')
            valid_count, invalid_count, partition_count = memory_based_processing(obj, filename)
        else:
            # logger.debug('using filesystem_based_processing...')
            valid_count, invalid_count, partition_count = filesystem_based_processing(obj, filename)

        if valid_count:
            result_code = 'Succeeded'
            result_string = f"{valid_count} records written across {partition_count} partitions. Original object size {obj.content_length} bytes"
            if invalid_count:
                result_string += f" {invalid_count} invalid records."
            logger.info(f"file {filename}: {result_string}")

        else:
            # TODO better to raise Exception here?
            result_code = 'PermanentFailure'
            result_string = f"no valid records. {invalid_count} invalid records"
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
