import json
import logging
import os
import time
import boto3
from datetime import datetime
from datetime import timezone

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

TABLE = os.getenv('ORDERS_TABLE', default='bathy-orders')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)


def update_dataset(order_id, dataset, output_location, status, ttl, now):
    # TODO add constraint to reject update if item does not already exist
    # use ExpressionAttributeNames since status,ttl are reserved words
    response = table.update_item(
        Key={
            'PK': 'ORDER#' + order_id,
            'SK': 'DATASET#' + dataset
        },
        UpdateExpression="SET #status = :status, last_update = :now, #ttl = :ttl, output_location = :output_location",
        ExpressionAttributeValues={
            ':status': status,
            ':now': now,
            ':ttl': ttl,
            ':output_location': output_location
        },
        ExpressionAttributeNames={
            "#status": "status",
            "#ttl": "TTL"
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise Exception("failed to update dataset")


def update_order(order_id, output_location, status, ttl, now):
    response = table.update_item(
        Key={
            'PK': 'ORDER#' + order_id,
            'SK': 'ORDER'
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
        raise Exception("failed to update order")


def lambda_handler(event, context):
    """
    update DynamoDB record for order's dataset
    """
    try:
        order_id = event['order_id']
        status = event['status']
        dataset = event['label']
        output_location = event['output_location']

        now = datetime.now(timezone.utc).isoformat(timespec='seconds')
        # expire records 60 days after last update
        ttl = int(time.time()) + (60 * 24 * 60 * 60)

        update_dataset(order_id=order_id, dataset=dataset, output_location=output_location, status=status, ttl=ttl, now=now)
        #update_order(order_id=order_id, output_location=output_location, status=f'{dataset} complete', ttl=ttl, now=now)

        return {
            'label': dataset,
            'output_location': output_location
        }

    except Exception as e:
        # generally due to missing required parameter in payload
        logger.error(e)
        raise e
