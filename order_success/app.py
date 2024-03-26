from datetime import timezone
from datetime import datetime
from datetime import timedelta
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import os
import logging
import boto3

TABLE = os.getenv('ORDERS_TABLE', default='bathy-orders')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))


def update_order(order_id, output_location, status='complete'):
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    print(f"updating order {order_id} status to {status}")
    # TODO add constraint to reject update if item does not already exist
    # use ExpressionAttributeNames since status,ttl are reserved words
    response = table.update_item(
        Key={
            'PK': 'ORDER#' + order_id,
            'SK': 'ORDER'
        },
        UpdateExpression='SET output_location = :output_location, #status = :status, last_update = :now',
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


def format_message(output_location):
    now = datetime.now(timezone.utc)
    expiration_date = now + timedelta(days=7)

    # convert s3 location to URL
    bucket_name, filename = output_location.split('/')[-2:]
    url = f'https://{bucket_name}.s3.amazonaws.com/{filename}'

    return f"""Your data request is ready and can be downloaded from {url}.\nThe data will be available until {expiration_date.strftime('%B %-d, %Y')}."""


def lambda_handler(event, context):
    print(event)
    order_id = event['order_id']
    output_location = event['output_location']
    datasets = event['datasets']

    if not output_location:
        # grid not created, use CSB extract as order output
        csb_dataset = [dataset for dataset in datasets if dataset['label'] == 'csb'][0]
        output_location = csb_dataset['output_location']

    # construct message for notification email
    msg = format_message(output_location)

    # update database with output_location
    update_order(order_id, output_location)

    return {
        "message": msg
    }
