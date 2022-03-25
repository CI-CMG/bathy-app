import json
import logging
import os
import time
import boto3
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


def update_item(order_id, dataset, output_location=None, status='SUCCEEDED'):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE)

    now = datetime.now().isoformat(timespec='seconds')
    # expire records 60 days after last update
    ttl = int(time.time()) + (60 * 24 * 60 * 60)

    # TODO add constraint to reject update if item does not already exist
    # use ExpressionAttributeNames since status,ttl are reserved words
    response = table.update_item(
        Key={
            'PK': 'ORDER#' + order_id,
            'SK': 'DATASET#' + dataset
        },
        UpdateExpression="SET #new_status = :status, last_update = :now, #ttl = :ttl, output_location = :output_location",
        ExpressionAttributeValues={
            ':status': status,
            ':now': now,
            ':ttl': ttl,
            ':output_location': output_location
        },
        ExpressionAttributeNames={
            "#new_status": "status",
            "#ttl": "TTL"
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise Exception("failed to update item")


def lambda_handler(event, context):
    """
    update DynamoDB record for order's dataset
    """

    try:
        order_id = event['order_id']
        status = event['status']
        dataset = event['type']
        output_location = None

        if 'output_location' in event:
            output_location = event['output_location']
        update_item(order_id, dataset, output_location, status)

        return {'status': 'SUCCESS'}

    except Exception as e:
        # generally due to missing required parameter in payload
        logger.error(e)
        return {'status': 'FAILURE'}
