from datetime import timezone
from datetime import datetime
from datetime import timedelta
import smtplib
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import os
import json
import logging
import boto3
from boto3.dynamodb.conditions import Key
import time

SMTP_HOST = '10.58.150.68'
SMTP_PORT = 25
TABLE = os.getenv('ORDERS_TABLE', default='bathy-orders')
SENDER_ADDRESS = os.getenv("SENDER", 'mb.info@noaa.gov')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)
server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))


def send_email(recipient, message):
    server.connect(host=SMTP_HOST, port=SMTP_PORT)
    server.sendmail(SENDER_ADDRESS, recipient, message)
    server.quit()


def format_message(recipient, url):
    now = datetime.now(timezone.utc)
    expiration_date = now + timedelta(days=7)

    return f"""From: NCEI/DCDB Bathymetry Data Manager <{SENDER_ADDRESS}>
To: {recipient}
Subject: Bathymetry Data Request

Your data request is ready and can be downloaded from {url}.  The data will be available until {expiration_date.strftime('%B %-d, %Y')}.
    """


def get_order(order_id):
    # get the ORDER item and all DATASETs
    response = table.query(
        KeyConditionExpression=Key('PK').eq('ORDER#' + order_id),
        ProjectionExpression="PK, SK, email, output_location"
    )
    items = response['Items']
    print('ORDER#' + order_id)
    print(items)
    # should be one ORDER item and at least one DATASET item
    if len(items) < 2:
        raise Exception(f'missing item(s) found for order ${order_id}')
    return items


def get_dataset_output_location(items):
    dataset_item = next(filter(lambda i: i['SK'].startswith('DATASET#') and 'output_location' in i, items))
    # may eventually store explicit 'item' attribute rather then inferring from SortKey
    type = dataset_item['SK'].split('#')[1]
    return dataset_item['output_location']


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


def lambda_handler(event, context):
    logger.debug(event)

    records = event['Records']
    for record in records:
        body = json.loads(record['body'])
        # order_id = body['order_id']
        # items = get_order(order_id)
        # order_item = next(filter(lambda i: i['SK'] == 'ORDER', items))
        recipient = event['email']
        msg = event['message']
        # output_location = order_item['output_location'] if 'output_location' in order_item else None
        # if not output_location:
        #     # presumably no grid requested, use first output_location found in dataset items
        #     output_location = get_dataset_output_location(items)
        #
        # # convert s3 location to URL
        # bucket_name, filename = output_location.split('/')[-2:]
        # url = f'https://{bucket_name}.s3.amazonaws.com/{filename}'
        #
        # msg = format_message(recipient, url)
        send_email(recipient, msg)
        # update_order(order_id, "complete")






