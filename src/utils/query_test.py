import requests
from requests.exceptions import Timeout
from urllib3.exceptions import ConnectTimeoutError
import uuid
import boto3
import urllib3
timeout = urllib3.util.Timeout(connect=1.0, read=5.0)

session = boto3.Session(profile_name='mfa')
s3 = session.resource('s3')
s3_key = str(uuid.uuid4()) + '.txt'
bucket = s3.Object(bucket_name='csb-pilot-delivery', key=s3_key)
print(bucket)

msg = {'query_params': {'type': 'multibeam', 'platform': 'Whiting'}, 'bbox': '-98.150,27.451,-96.018,28.807', 'TaskToken': 'AAAAKgAAAAIAAAAAAAAAAXNeSpejfhLUaGbnaZoswMyqlV5LctJxyMQeMfzTiFZL9cELj7h35fhHJS2caCOd1PDXTQKlOJHchVhDn7X9sQdiiJF0vsq0PkfguRnSqZdPTvsqGNY/fFmnONzZvR8J73yWi3v/FcWhwLldevDYg49w7OcT+gJffsoRBCt+BUhcqBRm01DMz4kc0gRf3DZv9rZ4FlyZnc7jCHYKsJQFgBFWZypHy8YT1LTpMTL2qvddQuPahGMfqp6E4IGGgDshrxoMUVljy/XjYbfedLue6jQH3YiOGEB2ZUgNCFzHA2ZCHhkXAIsaXaBgdI3ZBig+e7ajxeuK6f9nTziHR2cxtuKdYLceY1v27t3avd3s+ngOsARtY1PWH24SXfzedT+wiZ0jmCgGfCOfPJNxBT9ihHC4mHbYH8ev9pQCBJv1ODX2NN1fIOwNWL2pO43tx55hlrSU+hniNeepR6k6qXV1eJOXZyWCKwuv2nKArJGLumPox6Z26mUDJElPlajdXhPc1Jc0hfqwnmd9Nf3MrCuIlEeMLfrqBYw7WYpWzb5fQdn646LT9RHvLNNbhdaEBwumq3tqfuokHeXgvKUM3IjNoe5FMvsGHbScTH3JWLIA6uZpx4wR/YuMqZ6G1F/qxZobol5Sh6Tr1kZVdqFrIAErTXY=', 'order_id': '8e51af10-7129-4e79-8c04-566e9bd78f8c'}

payload = {'geometry': msg['bbox']}
if 'platform' in msg['query_params']:
    payload['platform'] = msg['query_params']['platform']
try:
    r = requests.get('https://gis.ngdc.noaa.gov/mapviewer-support/multibeam/catalog.groovy', params=payload, timeout=30)
    if r.status_code != 200:
        raise Exception('invalid response code: '+r.status_code)
except Exception as e:
    print('Failed to connect: '+str(e))
    raise Exception("Failed to connect")
# for line in r.iter_lines():
#     print(line)
# result = bucket.put(Body=r.text)
# print(result)

timeout = urllib3.util.Timeout(connect=1, read=20)
http = urllib3.PoolManager(timeout=timeout)
response = http.request("GET",
                        "https://gis.ngdc.noaa.gov/mapviewer-support/multibeam/catalog.groovy",
                        fields=payload)
print(response.data.decode("utf-8"))
response.data