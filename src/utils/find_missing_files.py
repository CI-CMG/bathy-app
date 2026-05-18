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

output_file = open(r'/Users/jcc/missing-files.csv', 'w')

all_files = []
manifest_file_name = r'/Users/jcc/noaa-dcdb-bathymetry-pds.inventory.csv'
with open(manifest_file_name, 'r') as manifest:
    for line in manifest:
        object_key = line.strip().split(',')[1]
        file_uuid = object_key.split('/')[-1][:-14]
        all_files.append(file_uuid)

loaded_files = []
with open(r'/Users/jcc/file_uuid_results', 'r') as uuid_manifest:
    for line in uuid_manifest:
        object_key = line.strip().replace('"',"")
        loaded_files.append(object_key)

print(sorted(loaded_files)[:5])
print(sorted(all_files)[:5])
# for i in all_files:
#     if i not in loaded_files:
#         print(i)

missing = set(sorted(all_files)).difference(sorted(loaded_files))
# print(list(missing)[:5])
for i in sorted(missing):
    year = i[:4]
    month = i[4:6]
    day = i[6:8]
    output_file.write(f'noaa-dcdb-bathymetry-pds,csb/csv/{year}/{month}/{day}/{i}_pointData.csv\n')

print(f'{len(missing)} files not loaded')

output_file.close()
