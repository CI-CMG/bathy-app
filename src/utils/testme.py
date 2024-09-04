import json
import boto3
import uuid
import logging
import random
import os

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))

client = boto3.client('stepfunctions')


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
    logger.info(event)

    counter = 0
    records = event['Records']
    for record in records:
        body = json.loads(record['body'])
        task_token = body['TaskToken']

        status = random.choice([0, 1, 2])
        logger.info(f'status is {str(status)}')
        payload = {
            'status': 'SUCCESS',
        }

        try:
            if status == 0:
                logger.info("sending success to step function")
                response = send_success(task_token, payload)
            elif status == 1:
                logger.info('throwing Exception...')
                raise Exception("Lambda threw exception")
            elif status == 2:
                logger.info("sending success to step function but using invalid task_token")
                response = send_success('invalid token', payload)

            counter = counter + 1

        except Exception as e:
            logger.error(e)
            logger.debug('sending failure to step function')
            response = send_failure(task_token, error_code='1', error_cause=str(e))

    print(f'processed {counter} out of {len(records)} records')
