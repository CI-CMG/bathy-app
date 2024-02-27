import boto3
from botocore import UNSIGNED
from botocore.client import Config

# s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
completion_report = "/Users/jcc/Downloads/7d7b9780aa79a04a24db4c012faba88bb073e781.csv"
BUCKET_NAME = 'noaa-bathymetry-pds'

s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))


def get_object_size(obj_key):
    obj = s3.Object(BUCKET_NAME, obj_key)
    # print(f"file {obj_key} has {obj.content_length} bytes")
    if obj.content_length < 1000000:
        print(f"{obj_key}: {obj.content_length}")
    return obj.content_length


with open(completion_report, 'r') as f:
    file_sizes = []
    for line in f:
        bucket,obj_key,_,status,status_code,state,message = line.strip().split(',')
        if "PermanentFailure: no valid records" in message:
            continue
        file_sizes.append(get_object_size(obj_key))
    avg = round(((sum(file_sizes) / len(file_sizes)) / 1048576), 2)
    print(f"{len(file_sizes)} files with average size of {avg}. Min {min(file_sizes)}, Max {max(file_sizes)}" )