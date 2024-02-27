import json
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import logging
import os
import time
from datetime import timezone
from boto3.dynamodb.conditions import Key

AWS_REGION = "us-east-1"
ORDER_ID = '3e66c3c4-8639-4955-bca7-a54d8020bc91'
TABLE = os.getenv('ORDERS_TABLE', default='bathy-orders')

# setup logging
log_level = os.getenv('LOGLEVEL', default='WARNING').upper()
try:
    log_level = getattr(logging, log_level)
except:
    # use default in case of invalid log level
    log_level = getattr(logging, 'WARNING')
logger = logging.getLogger(__name__)
logger.setLevel(log_level)

session = boto3.Session(profile_name='mfa')
dynamodb = session.resource('dynamodb', region_name=AWS_REGION)
# dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)


def get_output_locations(order_id):
    response = table.query(
        KeyConditionExpression=
        Key('PK').eq('ORDER#' + order_id) &
        Key('SK').begins_with('DATASET')
    )
    items = response['Items']
    if len(items) < 1:
        raise Exception(f'no datasets items found for order ${order_id}')

    return {i['SK'].split('#')[1]:i['output_location'] for i in items if 'output_location' in i}


def update_order(order_id, status):
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    # expire records 60 days after last update
    ttl = int(time.time()) + (60 * 24 * 60 * 60)
    print(f"updating order {order_id} status to {status}")
    # TODO add constraint to reject update if item does not already exist
    # use ExpressionAttributeNames since status,ttl are reserved words
    response = table.update_item(
        Key={
            'PK': 'ORDER#' + order_id,
            'SK': 'ORDER'
        },
        UpdateExpression='SET #status = :status, last_update = :now, #ttl = :ttl',
        ExpressionAttributeValues={
            ':status': status,
            ':now': now,
            ':ttl': ttl
        },
        ExpressionAttributeNames={
            "#status": "status",
            "#ttl": "TTL"
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise Exception("failed to update item")


def get_grid_params(order_id):
    response = table.get_item(
        Key={'PK': 'ORDER#' + order_id, 'SK': 'ORDER'},
        ProjectionExpression='bbox,grid'
    )
    if 'Item' not in response:
        raise Exception(f'no order found for id ${order_id}')
    bbox = [float(i) for i in response['Item']['bbox'].split(',')]
    # Boto3 deserializes to Decimal types
    format = int(response['Item']['grid']['format'])
    resolution = int(response['Item']['grid']['resolution'])
    return {'format': format, 'resolution': resolution, 'bbox': bbox}


def get_order_status(order_id):
    response = table.get_item(
        Key={'PK': 'ORDER#' + order_id, 'SK': 'ORDER'},
        ProjectionExpression="#status, last_update, output_location",
        ExpressionAttributeNames={
            "#status": "status"
        }
    )
    if 'Item' not in response:
        raise Exception(f'no order found for id ${order_id}')

    print(response['Item'])


# output_locations = get_output_locations(ORDER_ID)
# bbox = get_bbox('3adda880-5fcd-4455-8765-0d16cfcaa1cd')
# print(bbox)
# grid_params = get_grid_params('8492cbd7-f9b1-4bcc-b88f-126696f045c4')
# print(grid_params)
try:
    get_order_status('f437f5dd-ed68-48b6-9bb1-5d54b45559cc1')
except Exception as e:
    print('error in get_order_status')
    print(e)

# try:
#     print(f'querying for order id {ORDER_ID}...')
#     table.update_item(
#         Key={
#             'query_id': attributes['query_id']
#         },
#         UpdateExpression='SET query_status = :status, last_update = :timestamp',
#         ExpressionAttributeValues={
#             ':status': attributes['query_status'],
#             ':timestamp': int(datetime.timestamp(datetime.now()))
#         },
#         ConditionExpression = 'attribute_exists(query_id)'
#     )
#
# except ClientError as e:
#     print(e.response['Error']['Message'])
