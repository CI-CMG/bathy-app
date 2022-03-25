import json
import boto3

client = boto3.client('stepfunctions')


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


def lambda_handler(event, context):
    """mock the staging of multibeam data on the EC2 instance"""
    # print(event)

    counter = 0
    records = event['Records']
    for record in records:
        body = json.loads(record['body'])
        message = body['Message']
        task_token = body['TaskToken']
        try:
            payload = {
                'status': 'SUCCESS',
                'message': 'successfully staged Multibeam data'
            }
            response = send_success(task_token, payload)
            # response = send_failure(task_token, error_code='1', error_cause='error executing task')
            counter = counter + 1
        except Exception as e:
            print(str(e))

    print(f'processed {counter} out of {len(records)} records')
