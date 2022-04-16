import json
import logging
import os
import time
import boto3
from datetime import datetime
from datetime import timezone
from boto3.dynamodb.conditions import Key

# setup logging
log_level = os.getenv('LOGLEVEL', default='WARNING').upper()
try:
    log_level = getattr(logging, log_level)
except:
    # use default in case of invalid log level
    log_level = getattr(logging, 'WARNING')
logger = logging.getLogger(__name__)
logger.setLevel(log_level)

TABLE = os.getenv('ORDERS_TABLE', default='bathy-orders')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)


def all_datasets_complete(order_id):
    response = table.query(
        KeyConditionExpression=
        Key('PK').eq('ORDER#' + order_id) &
        Key('SK').begins_with('DATASET')
    )
    items = response['Items']
    if len(items) < 1:
        raise Exception(f'no datasets items found for order ${order_id}')

    # depends on string defined in step function definition
    completed = [i['status'] == 'complete' for i in response['Items']]
    return all(completed)


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


def lambda_handler(event, context):
    """
    verify that each dataset in the specified order is staged for further
    processing or delivery
    """
    if 'order_id' not in event:
        raise Exception('missing order_id')

    order_id = event['order_id']

    if not all_datasets_complete(order_id):
        raise Exception("datasets are not staged correctly")

    update_order(order_id, status="data staged")

    return {
        'order_id': order_id,
        'status': 'SUCCESS'
    }
