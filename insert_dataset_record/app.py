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
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)


def get_item(PK, SK):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE)

    response = table.get_item(
        Key={
            'PK': PK,
            'SK': SK
        }
    )


def insert_item(order_id, dataset_attributes):
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    # expire records 60 days after creation
    ttl = int(time.time()) + (60 * 24 * 60 * 60)
    attributes = {
        'PK': 'ORDER#' + order_id,
        'SK': 'DATASET#multibeam',
        'other': dataset_attributes
    }

    response = table.put_item(
        Item=attributes
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise Exception('insert into database failed')
    return attributes


def lambda_handler(event, context):
    """
    insert new Dataset record into DynamoDB orders table
    """
    print(event)
    if 'order_id' not in event or 'dataset' not in event:
        raise Exception("invalid payload. must contain order_id and dataset elements")

    # try:
    #
    #     attributes = insert_item(order_id=event['order_id'], email=event['email'], bbox=event['bbox'], grid=grid)
    #     # get_item(attributes['PK'], attributes['SK'])
    #     return json.dumps(attributes)
    #
    # except Exception as e:
    #     logger.error(e)
    #     print(e)
    #     # TODO better error response

    return event['dataset']

