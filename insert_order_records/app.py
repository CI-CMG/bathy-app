"""
insert the DynamoDB records for parent order and child datasets
"""
import logging
import os
import time
import uuid

import boto3
from datetime import datetime
from datetime import timezone

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.getenv('ORDERS_TABLE', default='bathy-orders'))


def insert_order_item(order_id, email, bbox, status='initialized', grid=None):
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    # expire records 60 days after creation
    ttl = int(time.time()) + (60 * 24 * 60 * 60)
    # convert bbox coords to strings to work around "Float types are not supported. Use Decimal types instead." error
    attributes = {
        'PK': 'ORDER#' + order_id,
        'SK': 'ORDER',
        'email': email,
        'bbox': [str(i) for i in bbox],
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


def insert_dataset_item(order_id, dataset_type, status='initialized'):
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    # expire records 60 days after creation
    ttl = int(time.time()) + (60 * 24 * 60 * 60)
    # convert bbox coords to strings to work around "Float types are not supported. Use Decimal types instead." error
    attributes = {
        'PK': 'ORDER#' + order_id,
        'SK': 'DATASET#' + dataset_type,
        'status': status,
        'last_update': now,
        'TTL': ttl
    }
    response = table.put_item(
        Item=attributes
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise Exception('insert into database failed')


def lambda_handler(event, context):
    # 'grid','email' are optional parameters
    grid = None
    if 'grid' in event:
        grid = event['grid']
    email = None
    if 'email' in event:
        email = event['email']

    order_id = str(event['order_id'])
    insert_order_item(order_id=order_id, email=email, bbox=event['bbox'], status='processing', grid=grid)

    for dataset in event['datasets']:
        insert_dataset_item(order_id=order_id, dataset_type=dataset['label'], status='processing')

# sample payload
# {
#   "email": "clreeves@akenergyauthority.org",
#   "bbox": [
#     -151.5351,
#     60.7228,
#     -151.2783,
#     60.8712
#   ],
#   "datasets": [
#     {
#       "label": "csb"
#     }
#   ],
#   "grid": {
#     "resolution": 5,
#     "format": 4
#   },
#   "order_id": "43fe4143-aab4-4916-8d51-a949b0ad6e71"
# }


