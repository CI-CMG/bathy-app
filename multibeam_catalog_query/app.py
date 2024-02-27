import json
import boto3
import requests
import uuid
import logging
import os
from utils import payload_to_sql

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

output_bucket = os.getenv('OUTPUT_BUCKET')
catalog_url = os.getenv('CATALOG_URL')

client = boto3.client('stepfunctions')
s3 = boto3.resource('s3')


def send_success(task_token, payload=None):
    response = client.send_task_success(
        taskToken=task_token,
        output=json.dumps(payload)
    )
    return response


def send_failure(task_token, error_code='', error_cause=''):
    response = client.send_task_failure(
        taskToken=task_token,
        error=error_code,
        cause=error_cause
    )
    return response


def lambda_handler(event, context):
    """query the multibeam catalog"""
    logger.info(event)

    counter = 0
    records = event['Records']
    for record in records:
        body = json.loads(record['body'])
        task_token = body['TaskToken']
        order_id = body['order_id']

        sql = payload_to_sql(body['query_params'])
        print(sql)

        params = {
            "where": sql,
            "outFields": "DATA_FILE",
            "returnGeometry": "false",
            "f": "json"
        }
        try:
            r = requests.get(catalog_url, params=params, timeout=10)
            if r.status_code != 200:
                logger.error('invalid response code: ' + str(r.status_code))
            payload = r.json()
            names = [x['attributes']['DATA_FILE'] for x in payload['features'] if
                     x['attributes']['DATA_FILE'] is not None]
            print(names)
            # process each line of catalog result? count lines?
            # for line in r.iter_lines():
            #     print(line)

            # write output
            s3_key = order_id + '_mbfiles.txt'
            mb_files_manifest = s3.Object(bucket_name=output_bucket, key=s3_key)
            result = mb_files_manifest.put(Body=r.text)

            # respond to step function
            payload = {
                'status': 'SUCCESS',
                'message': 'successfully queried multibeam catalog',
                'output_location': f's3://{output_bucket}/{s3_key}'
            }
            logger.debug("sending success to step function")
            response = send_success(task_token, payload)
            counter = counter + 1

        except Exception as e:
            logger.error(e)
            logger.debug('sending failure to step function')
            response = send_failure(task_token, error_code='1', error_cause='catalog query failed')

    print(f'processed {counter} out of {len(records)} records')