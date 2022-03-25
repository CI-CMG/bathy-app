import json
import boto3
from datetime import datetime
# import csb_support
import logging
import os
import utils
from utils import IllegalArgumentException
from utils import StateMachineException
import uuid
import time
import copy


# setup logging
log_level = os.getenv('LOGLEVEL', default='WARNING').upper()
try:
    log_level = getattr(logging, log_level)
except:
    # use default in case of invalid log level
    log_level = getattr(logging, 'WARNING')
logger = logging.getLogger(__name__)
logger.setLevel(log_level)


def lambda_handler(event, context):
    # random UUID to identify order and step function execution
    order_id = str(uuid.uuid4())

    client = boto3.client('stepfunctions')
    # TODO get from env
    # step_function_arn = 'arn:aws:states:us-east-1:282856304593:stateMachine:FlowcontrolTest'
    step_function_arn = 'arn:aws:states:us-east-1:282856304593:stateMachine:BathymetryStateMachine-agTM4lMdyLPz'

    try:
        if 'body' not in event:
            raise IllegalArgumentException('no body provided')

        payload = json.loads(event['body'])
        logger.debug(payload)
        payload['order_id'] = order_id
        # logger.debug(attributes)
        # logger.debug(bbox)

        # TODO validate payload

        response = client.start_execution(
            stateMachineArn=step_function_arn,
            name=order_id,
            input=json.dumps(payload)
        )
        # e.g.
        # {
        #   'executionArn': 'arn:aws:states:us-east-1:282856304593:execution:FlowcontrolTest:67fc3dc1-65bd-4d45-bc47-c49ade6c1a32',
        #   'startDate': datetime.datetime(2022, 3, 21, 23, 0, 42, 439000, tzinfo=tzlocal()),
        #   'ResponseMetadata': {
        #     'RequestId': 'e8b8153a-eada-46ba-a08c-e21a741253c5',
        #     'HTTPStatusCode': 200,
        #     'HTTPHeaders': {
        #       'x-amzn-requestid': 'e8b8153a-eada-46ba-a08c-e21a741253c5',
        #       'content-type': 'application/x-amz-json-1.0',
        #       'content-length': '148'
        #     },
        #     'RetryAttempts': 0
        #   }
        # }
        # print(response)
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise StateMachineException('error executing state machine')

        # TODO add URL to check the status of the given order
        response_body = {
            "message": f"extract request {order_id} created."
        }

        return {
            'statusCode': 201,
            'headers': {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps(response_body)
        }

    except IllegalArgumentException as e:
        logger.error("invalid payload in request")
        logger.debug(e)
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': "application/json"
            },
            'body': json.dumps(e.args[0])
        }

    except StateMachineException as e:
        logger.error("invalid payload in request")
        logger.debug(e)
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': "application/json"
            },
            # 'body': json.dumps(e.args[0])
            'body': str(e)
    }

    except Exception as e:
        logger.debug('untyped exception')
        logger.debug(e)
        logger.error(e.args[0])

        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': "application/json"
            },
            'body': json.dumps(e.args[0])
        }