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


def update_item(order_id, dataset, output_location=None):
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
        UpdateExpression="SET #status = :status, last_update = :now, #ttl = :ttl, output_location = :output_location",
        ExpressionAttributeValues={
            ':status': 'error',
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
        raise Exception("failed to update item")


def lambda_handler(event, context):
    """
    handle errors in the dataset-specific processing part of StepFunction. Includes update of the DynamoDB item
    and may eventually include notification
    """
    try:
        order_id = event['order_id']
        dataset = event['type']
        cause = json.loads(event['body']['Cause'])
        update_item(order_id=order_id, dataset=dataset)

    except Exception as e:
        # generally due to missing required parameter in payload
        logger.error(e)
        raise e

# sample Athena error response
# {
#     'QueryExecution': {
#         'EngineVersion': {
#             'EffectiveEngineVersion': 'Athena engine version 3', 'SelectedEngineVersion': 'AUTO'
#         },
#         'Query': 'SELECT lon,lat,depth,time,platform_name1,provider FROM dcdb.csb_parquet where lon > 5 and lon < 6 and lat > 60 and lat < 61',
#         'QueryExecutionContext': {},
#         'QueryExecutionId': '71a69f3e-37d8-4883-9b51-5ed3a8c9376b',
#         'ResultConfiguration': {'OutputLocation': 's3://order-pickup/71a69f3e-37d8-4883-9b51-5ed3a8c9376b.csv'},
#         'ResultReuseConfiguration': {
#             'ResultReuseByAgeConfiguration': {'Enabled': False}
#         },
#         'StatementType': 'DML',
#         'Statistics': {
#             'DataScannedInBytes': 0,
#             'EngineExecutionTimeInMillis': 249,
#             'QueryQueueTimeInMillis': 104,
#             'ResultReuseInformation': {'ReusedPreviousResult': False},
#             'ServicePreProcessingTimeInMillis': 83,
#             'ServiceProcessingTimeInMillis': 21,
#             'TotalExecutionTimeInMillis': 457
#         },
#         'Status': {
#             'AthenaError': {
#                 'ErrorCategory': 2,
#                 'ErrorMessage': "COLUMN_NOT_FOUND: line 1:27: Column 'platform_name1' cannot be resolved or requester is not authorized to access requested resources",
#                 'ErrorType': 1006, 'Retryable': False
#             },
#             'CompletionDateTime': 1710623587301,
#             'State': 'FAILED',
#             'StateChangeReason': "COLUMN_NOT_FOUND: line 1:27: Column 'platform_name1' cannot be resolved or requester is not authorized to access requested resources",
#             'SubmissionDateTime': 1710623586844
#         },
#         'SubstatementType': 'SELECT',
#         'WorkGroup': 'primary'
#     }
# }
