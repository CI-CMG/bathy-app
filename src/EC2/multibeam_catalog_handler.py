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
            if 'order_id' not in body or 'TaskToken' not in body:
                logger.error(f"message is missing order_id or TaskToken")
                message.delete()
                continue

            order_id = body['order_id']
            task_token = body['TaskToken']
            try:
                # simulate work being done...
                time.sleep(3)
                payload = {
                    'status': 'SUCCESS',
                    'message': 'successfully queried multibeam catalog'
                }
                response = send_success(task_token, payload)

            except Exception as e:
                logger.error(e)

            logger.debug(f'deleting message for order_id {order_id}')
            message.delete()
            # update_order_status(order_id, 'NOTIFIED')

        # wait before getting the next batch from the queue
        logger.debug(f"all messages processed. waiting for {SLEEP_MINUTES} minutes before checking again...")
        time.sleep(SLEEP_MINUTES*60)
    # end of infinite while loop


def send_success(task_token, payload=None):
    response = client.send_task_success(
        taskToken=task_token,
        output=json.dumps(payload)
    )
    return response


def send_failure(task_token, error_code='', error_cause=''):
    response = client.send_task_failure(
        taskToken=task_token,
        error=error_code,
        cause=error_cause
    )
    return response
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
        description="""monitor AWS queue and query multibeam catalog. Notify Step function when complete"""
    )
    arg_parser.add_argument("--profile", default="default", help="AWS profile")
    args = arg_parser.parse_args()

    SLEEP_MINUTES = 1                     # wait time before checking queue again
    QUEUE_NAME = 'MultibeamCatalogQueue'
    ORDERS_TABLE = 'bathy-orders'

    session = boto3.Session(profile_name=args.profile)
    sqs = session.resource('sqs')
    dynamodb = session.resource('dynamodb')
    client = boto3.client('stepfunctions')
    queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
    table = dynamodb.Table(ORDERS_TABLE)

    main()
