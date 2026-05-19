"""
notify user of successful completion. If no email provided, no action is taken
"""
import json
import logging
import os
import boto3
from datetime import timezone
from datetime import datetime
from datetime import timedelta

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))
notification_queue_url = os.environ['ORDER_NOTIFICATION_QUEUE_URL']

# TODO should the order status be changed from "completed" to "notified"?
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table(os.getenv('ORDERS_TABLE', default='bathy-orders'))
sqs = boto3.client('sqs')

def format_message(output_location: str):
    now = datetime.now(timezone.utc)
    expiration_date = now + timedelta(days=7)

    # convert s3 location to URL
    bucket_name, filename = output_location.split('/')[-2:]
    url = f'https://{bucket_name}.s3.amazonaws.com/{filename}'
    return f"""Your data request is ready and can be downloaded from {url}.\nThe data will be available until {expiration_date.strftime('%B %-d, %Y')}."""


def lambda_handler(event, context):
    order_id = event['order_id']
    original_input = event['input']

    # in case of order error, may not be an output_location
    if 'output_location' in event:
        output_location = str(event['output_location'])
    else:
        output_location = None

    email = None
    if 'email' in original_input:
        email = original_input['email']

    if not email:
        logger.info('No email provided so no notification is sent.')
        return {}

    # construct message for notification email
    if output_location:
        msg = format_message(output_location)
    else:
        msg = f"error processing order_id: {order_id}"

    # format expected by send_email_via_relay Lambda
    body = {
        "email": email,
        "message": msg
    }
    response = sqs.send_message(
        QueueUrl=notification_queue_url,
        MessageBody=json.dumps(body)
    )

    return response
