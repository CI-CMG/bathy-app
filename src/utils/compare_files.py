import boto3
from boto3.dynamodb.conditions import Key

AWS_REGION = "us-east-1"
session = boto3.Session(profile_name='mfa')
dynamodb = session.resource('dynamodb', region_name=AWS_REGION)
# dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('csb-processed-files')


def record_exists(line):
    object_key = line.strip().split(',')[1]
    pk = object_key.split('/')[-1][:6]

    response = table.query(KeyConditionExpression=Key('PK').eq(pk) & Key('SK').eq(object_key))
    items = response['Items']
    if response['Count']:
        return True
    else:
        print(object_key)
        return False


output_file = open(r'/Users/jcc/missing-files.2019.csv', 'w')

# manifest_file_name = r'/Users/jcc/noaa-dcdb-bathymetry-pds.inventory.csv'
manifest_file_name = r'/Users/jcc/noaa-dcdb-bathymetry-pds.inventory.2019.csv'
with open(manifest_file_name, 'r') as manifest:
    counter = 0
    for line in manifest:
        if not record_exists(line):
            output_file.write(line)
        counter = counter + 1

    print(f'checked {counter} files')

output_file.close()
