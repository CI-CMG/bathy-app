import json
import boto3
import logging
import os
from utils import query_mapservice

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

output_bucket = os.getenv('OUTPUT_BUCKET')
catalog_url = os.getenv('CATALOG_URL')

sfn_client = boto3.client('stepfunctions')
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')



def send_success(task_token, payload=None):
    response = sfn_client.send_task_success(
        taskToken=task_token,
        output=json.dumps(payload)
    )
    return response


def send_failure(task_token, error_code='', error_cause=''):
    response = sfn_client.send_task_failure(
        taskToken=task_token,
        error=error_code,
        cause=error_cause
    )
    return response


def lambda_handler(event, context):
    """query the multibeam catalog"""
    logger.info(event)

    task_token = event['TaskToken']
    order_id = event['order_id']
    dataset = event['dataset']
    label = dataset['label']
    bbox = event['bbox'] if 'bbox' in event else None

    try:
        # files listed in mapservice may not actually exist in S3
        fbt_files = query_mapservice(bbox=bbox, query_params=dataset)
        logger.info(f'found {len(fbt_files)} files')

        # write output
        s3_key = order_id + '_mbfiles.json'
        s3_client.put_object(
            Bucket=output_bucket,
            Key=s3_key,
            Body=json.dumps(fbt_files),
            ContentType='application/json'
        )
        logger.info(f'list of FBT files available at https://order-pickup.s3.us-east-1.amazonaws.com/{s3_key}')

        # respond to step function
        payload = {
            'label': label,
            'output_location': f's3://{output_bucket}/{s3_key}'
        }
        logger.debug("sending success to step function")
        send_success(task_token, payload)

    except Exception as e:
        logger.error(e)
        logger.debug('sending failure to step function')
        send_failure(task_token, error_code='1', error_cause='catalog query failed')
