import json
import logging
import os
import time
import boto3
import uuid
from datetime import datetime

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
    # expire records 60 days after creation
    ttl = int(time.time()) + (60 * 24 * 60 * 60)
    attributes = {
        'PK': 'ORDER#' + order_id,
        'SK': 'ORDER',
        'email': email,
        'bbox': bbox,
        'status': status,
        'last_update': datetime.now().isoformat(timespec='seconds'),
        'TTL': ttl
    }
    if grid:
        print('found grid...')
        attributes['grid'] = grid

    response = table.put_item(
        Item=attributes
    )
    if (response['ResponseMetadata']['HTTPStatusCode'] != 200):
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

        attributes = insert_item(order_id=event['order_id'], email=event['email'], bbox=event['bbox'], grid=grid)
        # get_item(attributes['PK'], attributes['SK'])
        return json.dumps(attributes)

    except Exception as e:
        logger.error(e)
        print(e)
        # TODO better error response



