import json
import logging
import os
import boto3
# import requests

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
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)


def get_order_status(order_id):
    response = table.get_item(
        Key={'PK': 'ORDER#' + order_id, 'SK': 'ORDER'},
        ProjectionExpression="#status, last_update, output_location",
        ExpressionAttributeNames={
            "#status": "status"
        }
    )
    if 'Item' not in response:
        raise NotFoundException(f'no order found for id ${order_id}')

    return response['Item']


def lambda_handler(event, context):
    try:
        order_id = event['pathParameters']['proxy']
        if not order_id:
            raise BadRequestException("order ID not provided")

        response = get_order_status(order_id)

    except NotFoundException as e:
        logger.warning(e.args[0])
        return {
            'statusCode': 404,
            'body': json.dumps(e.args[0])
        }
    except BadRequestException as e:
        logger.warning(e.args[0])
        return {
            'statusCode': 400,
            'body': json.dumps(e.args[0])
        }
    except Exception as e:
        logger.warning(e.args[0])
        return {
            'statusCode': 500,
            'body': json.dumps(e.args[0])
        }


    return {
        "statusCode": 200,
        "body": json.dumps(response)
        # "body": json.dumps({
        #     "message": f"status of order {order_id}: TODO"
        # })
    }


class BadRequestException(Exception):
    pass


class NotFoundException(Exception):
    pass
