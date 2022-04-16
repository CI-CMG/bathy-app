import json
import logging
import os
import time
import boto3
from datetime import datetime
from datetime import timezone

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


def update_item(order_id, dataset, status='FAILURE'):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE)

    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    # expire records 60 days after last update
    ttl = int(time.time()) + (60 * 24 * 60 * 60)

    # TODO add constraint to reject update if item does not already exist
    # use ExpressionAttributeNames since status,ttl are reserved words
    response = table.update_item(
        Key={
            'PK': 'ORDER#' + order_id,
            'SK': 'DATASET#' + dataset
        },
        UpdateExpression='SET #new_status = :status, last_update = :now, #ttl = :ttl',
        ExpressionAttributeValues={
            ':status': status,
            ':now': now,
            ':ttl': ttl
        },
        ExpressionAttributeNames={
            "#new_status": "status",
            "#ttl": "TTL"
        }
    )
    if (response['ResponseMetadata']['HTTPStatusCode'] != 200):
        raise Exception("failed to update item")


def lambda_handler(event, context):
    """
    handle errors in the dataset-specific processing part of StepFunction. Includes update of the DynamoDB item
    and may eventually include notification
    """
    try:
        order_id = event['order_id']
        status = event['status']
        dataset = event['type']
        update_item(order_id, dataset, status)

        return {'status': 'SUCCESS'}

    except Exception as e:
        # generally due to missing required parameter in payload
        logger.error(e)
        return {'status': 'FAILURE'}

