import json
import boto3
from botocore.exceptions import ClientError

response = {
        'result': False,
        'answer': '',
        'data': ''
    }

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)
bucket_name = 'aep'
key_path = 'data/speed​_calculations.json'

def getObject(bucket, key):
  get_object_response = s3.get_object(Bucket=bucket,Key=key)
  return get_object_response['Body'].read()

def putObject(bucket, key, data):
  s3.put_object(Bucket=bucket, Key=key, Body=data)

def handler(event, context):
    eventBody = event['body']
    data = json.loads(eventBody)
    dataList = json.loads(getObject(bucket_name, key_path))
    
    dataList.append(data)
    response['answer'] = 'Данные сохранены в облаке'

    putObject(bucket_name, key_path, json.dumps(dataList))
    response['data'] = 'Данных в облаке: ' + str(len(dataList))
    response['result'] = True
    
    return {
        'statusCode': 200,
        'headers': {
                "Access-Control-Allow-Headers": "Content-Type", 
                "Content-Type": "application/json; charset=utf-8",
            },
        
         'body': json.dumps(
            response, 
            default=vars,
         ),
    }