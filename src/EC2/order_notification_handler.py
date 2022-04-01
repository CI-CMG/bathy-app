import boto3
import logging
import json
import time
import argparse
from datetime import timezone
from datetime import datetime
from datetime import timedelta
import smtplib
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


def main():
    # run forever
    while True:
        # WaitTimeSeconds enables Long Polling
        messages = queue.receive_messages(WaitTimeSeconds=10)
        logger.debug(f"found {len(messages)} notifications in queue to process...")

        for message in messages:
            body = json.loads(message.body)
            if 'order_id' not in body or 'email' not in body:
                logger.error(f"message is missing order_id or email attributes")
                message.delete()
                continue

            order_id = body['order_id']
            email = body['email']
            output_url = get_output_url(order_id)
            send_email(recipient=email, url=output_url)
            logger.debug(f'deleting message for order_id {order_id}')
            message.delete()
            update_order_status(order_id, 'NOTIFIED')

        # wait before getting the next batch from the queue
        logger.debug(f"all messages processed. waiting for {SLEEP_MINUTES} minutes before checking again...")
        time.sleep(SLEEP_MINUTES*60)
    # end of infinite while loop


def get_output_url(order_id):
    """retrieve the output location for the CSV file and reformat into a URL"""
    table = dynamodb.Table(ORDERS_TABLE)
    response = table.query(
        KeyConditionExpression=
        Key('PK').eq('ORDER#'+order_id) &
        Key('SK').eq('DATASET#csb')
    )
    # should only be one CSB dataset per order
    if len(response['Items']) != 1:
        raise Exception(f'no CSB dataset records found for order Id {order_id}')

    s3_bucket = response['Items'][0]['output_location']
    bucket_name, filename = s3_bucket.split('/')[-2:]
    return f'https://{bucket_name}.s3.amazonaws.com/{filename}'


def send_email(recipient, url):
    logger.info(f"notifying {recipient} about {url}")
    sender_address = 'mb.info@noaa.gov'

    now = datetime.now(timezone.utc)
    expiration_date = now + timedelta(days=7)

    msg = f"""From: NCEI/DCDB Bathymetry Data Manager <{sender_address}>
To: {recipient}
Subject: Crowdsourced Bathymetry Data Request

Your data request is ready and can be downloaded from {url}.  The data will be available until {expiration_date.strftime('%B %w, %Y')}.
"""
    server = smtplib.SMTP('10.58.150.68', 25)
    #server.set_debuglevel(1)
    server.sendmail(sender_address, recipient, msg)
    server.quit()


def update_order_status(order_id, status='NOTIFIED'):
    # construct ISO8601 format string of current time w/o TZ offset
    #now = datetime.datetime.now(timezone.utc).isoformat(timespec='seconds')[:-6]
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    # expire records 60 days after last update
    ttl = int(time.time()) + (60 * 24 * 60 * 60)
    pk = 'ORDER#'+order_id
    try:
        table.update_item(
            Key={
                'PK': pk,
                'SK': 'ORDER'
            },
            UpdateExpression='SET #status = :status, last_update = :timestamp',
            ExpressionAttributeValues={
                ':status': status,
                ':timestamp': now,
                ':pk': pk,
                ':sk': 'ORDER'
            },
            ExpressionAttributeNames={
                "#status": "status"
            },
            ConditionExpression="PK = :pk and SK = :sk"
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            logger.error(e.response['Error']['Message'])
        else:
            raise


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    arg_parser = argparse.ArgumentParser(
        description="""monitor AWS queue and notify users that data are available for pickup"""
    )
    arg_parser.add_argument("--profile", default="default", help="AWS profile")
    args = arg_parser.parse_args()

    SLEEP_MINUTES = 1                     # wait time before checking queue again
    QUEUE_NAME = 'OrderNotificationQueue'
    QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/282856304593/OrderNotificationQueue'
    ORDERS_TABLE = 'bathy-orders'

    session = boto3.Session(profile_name=args.profile)
    sqs = session.resource('sqs')
    dynamodb = session.resource('dynamodb')
    queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
    table = dynamodb.Table(ORDERS_TABLE)

    main()
