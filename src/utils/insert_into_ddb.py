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
TABLE = 'orders-table-demo'

logger = logging.getLogger(__name__)
logger.setLevel(os.getenv('LOGLEVEL', default='INFO'))

session = boto3.Session(profile_name='mfa')
dynamodb = session.resource('dynamodb', region_name=AWS_REGION)
# dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)

payload = {
  "email": "john.cartwright@noaa.gov",
  "bbox": [
    5.0,
    60.0,
    6.0,
    61.0
  ],
  "datasets": [
    {
      "label": "csb",
      "platforms": [
        "Ramform Vanguard"
      ]
    }
  ],
  "order_id": "8a2888a4-9c19-48ac-9ad4-e73b1755fbfc"
}


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
        # 'bbox': [str(i) for i in bbox],
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


response = insert_item(
    order_id=payload['order_id'],
    email=payload['email'],
    bbox=payload['bbox']
)
print(response)

response = update_order(order_id=payload['order_id'], status='testing')
