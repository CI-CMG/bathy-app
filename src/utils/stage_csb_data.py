import json
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import logging
import os
import time
from datetime import timezone
from boto3.dynamodb.conditions import Key
from os import path

# setup logging
log_level = os.getenv('LOGLEVEL', default='DEBUG').upper()
try:
    log_level = getattr(logging, log_level)
except:
    # use default in case of invalid log level
    log_level = getattr(logging, 'DEBUG')
logger = logging.getLogger(__name__)
logger.setLevel(log_level)


session = boto3.Session(profile_name='mfa')
s3 = session.resource('s3')
s3 = session.client('s3')
INCOMING_DIR = '/Users/jcc/Downloads/'
csv_file_uri = 's3://csb-pilot-delivery/210dd2f9-d781-4106-9f9d-b7f9a05b4502.csv'
mb_file_uri = 's3://csb-pilot-delivery/8803e78e-5c20-408b-a3e7-e15b76aa29a6_mbfiles.txt'


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


csv_file = download_file_from_s3(csv_file_uri)
print(f"csv file is {csv_file}")
xyz_file = convert_csv_to_xyz(csv_file)
print(f"xyz file is {csv_file}")
mb_file = download_file_from_s3(mb_file_uri)
print(f"mb file is {mb_file}")

