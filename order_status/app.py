import json
import logging
import os
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


def lambda_handler(event, context):
    try:
        order_id = event['pathParameters']['proxy']
        if not order_id:
            raise IllegalArgumentException("order ID not provided")

    except IllegalArgumentException as e:
        logger.warning(e.args[0])
        return {
            'statusCode': 404,
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
        "body": json.dumps({
            "message": f"status of order {order_id}: TODO"
        })
    }


class IllegalArgumentException(Exception):
    pass
