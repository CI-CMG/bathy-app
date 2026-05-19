import json
import logging
import os
import time
import boto3
from datetime import datetime
from datetime import timezone

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.getenv('ORDERS_TABLE', default='bathy-orders'))

def update_order(order_id, status, output_location, now):
    response = table.update_item(
        Key={
            'PK': 'ORDER#' + order_id,
            'SK': 'ORDER'
        },
        UpdateExpression="SET #status = :status, last_update = :now, output_location = :output_location",
        ExpressionAttributeValues={
            ':status': status,
            ':now': now,
            ':output_location': output_location
        },
        ExpressionAttributeNames={
            "#status": "status"
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
        output_location = event['output_location']
        now = datetime.now(timezone.utc).isoformat(timespec='seconds')

        update_order(order_id=order_id, status=status, output_location=output_location, now=now)

        return {
            'output_location': output_location
        }

    except Exception as e:
        # generally due to missing required parameter in payload
        logger.error(e)
        raise e
