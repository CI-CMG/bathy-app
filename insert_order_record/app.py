import json
import logging
import os
import time
import boto3
import uuid
from datetime import datetime
from datetime import timezone

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

TABLE = os.getenv('ORDERS_TABLE', default='bathy-orders')


def get_item(PK, SK):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE)

    response = table.get_item(
        Key={
            'PK': PK,
            'SK': SK
        }
    )


def insert_item(order_id, email, bbox, status='initialized', grid=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE)
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    # expire records 60 days after creation
    ttl = int(time.time()) + (60 * 24 * 60 * 60)
    attributes = {
        'PK': 'ORDER#' + order_id,
        'SK': 'ORDER',
        'email': email,
        'bbox': bbox,
        'status': status,
        'last_update': now,
        'TTL': ttl
    }
    if grid:
        attributes['grid'] = grid

    response = table.put_item(
        Item=attributes
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise Exception('insert into database failed')
    return attributes


def lambda_handler(event, context):
    """
    insert new Order record into DynamoDB orders table
    """

    # 'grid' is only optional parameter
    grid = None
    if 'grid' in event:
        grid = event['grid']

    try:

        attributes = insert_item(order_id=event['order_id'], email=event['email'], bbox=event['bbox'], status='processing', grid=grid)
        # get_item(attributes['PK'], attributes['SK'])
        return json.dumps(attributes)

    except Exception as e:
        logger.error(e)
        print(e)
        # TODO better error response



