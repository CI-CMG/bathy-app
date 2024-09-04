"""
handles API request and returns a list of S3 object URLs based on query to ArcGIS map service
"""
import json
import logging
import os
import boto3
import requests
from urllib.parse import parse_qs
from urllib.parse import urlencode
import requests
from botocore.errorfactory import ClientError
base_url = 'https://gis.ngdc.noaa.gov/arcgis/rest/services/csb/MapServer/1/query?'

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

s3 = boto3.client('s3')


def construct_s3_url(filename):
    # e.g. '20190827100235229150_7cb9a8c2-5d2a-4c91-ac35-13fd2340a589.tar.gz
    year = filename[:4]
    month = filename[4:6]
    day = filename[6:8]
    file = filename[:-7]
    s3_key = f"csb/csv/{year}/{month}/{day}/{file}_pointData.csv"
    try:
        s3.head_object(Bucket='noaa-dcdb-bathymetry-pds', Key=s3_key)
    except ClientError:
        print(f'object {s3_key} not found')

    return 'https://noaa-dcdb-bathymetry-pds.s3.amazonaws.com/' + s3_key


def lambda_handler(event, context):
    print(event)

    query_params = event['queryStringParameters']

    if not len(query_params):
        return {
            'statusCode': 400,
            'body': 'at least one valid filter criteria must be specified'
        }

    arcgis_query_params = {
        'outFields': 'NAME',
        'returnGeometry': 'false',
        'f': 'pjson'
    }

    where = []
    # TODO what query_params to support? keep name/case same as ArGIS REST call?
    if 'PLATFORM' in query_params:
        # TODO expect query params string arguments to be quoted or not?
        # where.append(f"PLATFORM='{query_params['PLATFORM']}'")
        where.append(f"PLATFORM={query_params['PLATFORM']}")

    arcgis_query_params['where'] = ' AND '.join(where)
    arcgis_url = base_url + urlencode(arcgis_query_params)
    # print(arcgis_url)

    where = []

    if 'PLATFORM' in query_params:
        where.append(f"PLATFORM='{query_params['PLATFORM']}'")

    arcgis_query_params['where'] = ' AND '.join(where)
    r = requests.get(base_url, params=arcgis_query_params)
    payload = r.json()

    names = [construct_s3_url(x['attributes']['NAME']) for x in payload['features']]

    return {
        "statusCode": 200,
        "body": json.dumps(names)
    }
