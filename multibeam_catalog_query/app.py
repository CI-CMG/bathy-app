import json
import boto3
import requests
import uuid
import logging
import os


# setup logging
log_level = os.getenv('LOGLEVEL', default='WARNING').upper()
try:
    log_level = getattr(logging, log_level)
except:
    # use default in case of invalid log level
    log_level = getattr(logging, 'WARNING')
logger = logging.getLogger(__name__)
logger.setLevel(log_level)

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
    logger.debug(event)

    counter = 0
    records = event['Records']
    for record in records:
        body = json.loads(record['body'])
        task_token = body['TaskToken']
        order_id = body['order_id']

        # prepare/execute HTTP catalog request. request timeout should < Lambda execution limits
        payload = {'geometry': body['bbox']}
        if 'platform' in body['query_params']:
            payload['platform'] = body['query_params']['platform']
        # TODO add other supported parameters

        try:
            r = requests.get(catalog_url, params=payload, timeout=10)
            if r.status_code != 200:
                logger.error('invalid response code: ' + str(r.status_code))

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