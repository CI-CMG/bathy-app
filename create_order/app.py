import json
import boto3
from datetime import datetime
# import csb_support
import logging
import os
# import utils
# from utils import IllegalArgumentException
# from utils import StateMachineException
import uuid
import time
import copy
import jsonschema

STATE_MACHINE_ARN = os.environ.get("STATE_MACHINE_ARN")

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

# load payload schema definition
with open('pointstore_payload_schema.json', 'r') as file:
    payload_schema = json.load(file)


def valid_bbox(bbox):
    if not bbox:
        return False
    if isinstance(bbox, str):
        coords = [float(i) for i in bbox.split(',')]
    else:
        coords = bbox
    if len(coords) != 4:
        return False
    if coords[0] < -180 or coords[0] > 180 or coords[2] < -180 or coords[2] > 180:
        return False
    if coords[1] < -90 or coords[1] > 90 or coords[3] < -90 or coords[3] > 90:
        return False
    # crosses antimeridian
    if coords[0] >= coords[2]:
        return False
    if coords[1] == coords[3]:
        return False
    return True


def lambda_handler(event, context):
    # print(os.getenv('ORDER_ENDPOINT_URL'))
    if not STATE_MACHINE_ARN:
        raise Exception('missing environment variable for Step Function')

    # random UUID to identify order and step function execution
    order_id = str(uuid.uuid4())

    client = boto3.client('stepfunctions')

    try:
        if 'body' not in event:
            raise IllegalArgumentException('no body provided')

        payload = json.loads(event['body'])
        logger.debug(payload)
        payload['order_id'] = order_id

        # validate payload
        try:
            jsonschema.validate(instance=payload, schema=payload_schema)
        except jsonschema.exceptions.ValidationError as e:
            logger.warning(e.message)
            raise IllegalArgumentException(f'invalid payload format: failed to match JSON Schema')

        # accommodate legacy bbox string
        if isinstance(payload['bbox'], str):
            try:
                payload['bbox'] = [float(i.strip()) for i in payload['bbox'].split(',')]
            except ValueError as e:
                raise IllegalArgumentException('invalid payload format: bbox string must contain only numbers')

        if not valid_bbox(payload['bbox']):
            raise IllegalArgumentException(f'invalid payload format - bad bbox coordinates')

        response = client.start_execution(
            stateMachineArn=STATE_MACHINE_ARN,
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

        # construct endpoint URL as workaround to using env variable
        endpoint_url = f"https://{event['headers']['host']}{event['rawPath']}/"
        response_body = {
            "message": f"extract request {order_id} created.",
            "url": endpoint_url + order_id
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


class IllegalArgumentException(Exception):
    pass


class StateMachineException(Exception):
    pass
