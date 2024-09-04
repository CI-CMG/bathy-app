"""
demonstrate using ArcGIS map service to locate CSB files in S3 bucket
"""

import json
import boto3
import requests

import json
import boto3
from urllib.parse import parse_qs
from urllib.parse import urlencode
import requests
from botocore.errorfactory import ClientError

s3 = boto3.client('s3')

base_url = 'https://gis.ngdc.noaa.gov/arcgis/rest/services/csb/MapServer/1/query?'
# simulate URL query parameters
query_params = {
    'PLATFORM': 'Copper Star'
}

arcgis_query_params = {
    'outFields': 'NAME',
    'returnGeometry': 'false',
    'f': 'pjson'
}


def construct_s3_url(filename):
    # e.g. '20190827100235229150_7cb9a8c2-5d2a-4c91-ac35-13fd2340a589.tar.gz
    year = filename[:4]
    month = filename[4:6]
    day = filename[6:8]
    file = filename[:-7]
    s3_key = f"csb/csv/{year}/{month}/{day}/{file}_pointData.csv"
    # TODO better error handling
    try:
        s3.head_object(Bucket='noaa-dcdb-bathymetry-pds', Key=s3_key)
    except ClientError:
        print(f'object {s3_key} not found')

    return 'https://noaa-dcdb-bathymetry-pds.s3.amazonaws.com/' + s3_key


where = []

if 'PLATFORM' in query_params:
    where.append(f"PLATFORM='{query_params['PLATFORM']}'")

arcgis_query_params['where'] = ' AND '.join(where)
r = requests.get(base_url, params=arcgis_query_params)
payload = r.json()

names = [construct_s3_url(x['attributes']['NAME']) for x in payload['features']]
type(names)
print(names)
