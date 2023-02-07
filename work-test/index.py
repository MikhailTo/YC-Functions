import json
import yaml
import base64
import boto3
from botocore.exceptions import ClientError

bucket_name = 'pse'
key_path = 'data/new_answers.json'

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

response = {
        'result': False,
        'answer': '',
        'data': ''
    }

def getObject(bucket, key):
  get_object_response = s3.get_object(Bucket=bucket,Key=key)
  return get_object_response['Body'].read()

def putObject(bucket, key, data):
  s3.put_object(Bucket=bucket, Key=key, Body=data)

def preparationData(event):
    data = {}
    compressedData = event['body']
    stringData = base64.b64decode(compressedData).decode()
    yamlData = yaml.safe_load(stringData)
    ###############################################################
    if isinstance(yamlData, dict):  # Seriously, it is a dictionary.  Or modest dictionary. 
        data = dict(yamlData)       # But it needs to be asked about it... 
    return data                     # And if it really is the dictionary, 
                                    # then you need to make it the dictionary, 
                                    # and only then will he become what it is. 
                                    # Otherwise, it is some kind of a pathetic string. 
                                    # And it won't show you its a symbol because it's the f*cking dictionary!!!

def handler(event, context):
    data = preparationData(event)
    dataList = json.loads(getObject(bucket_name, key_path))
    
    isElem = False
    for elem in dataList:
        if elem is not None and data is not None:
            if (elem.keys() == data.keys()):
                isElem = True
                elem.update(data)
                response['answer'] = 'Вопрос обновлен в облаке'
    if (not isElem):
        dataList.append(data)
        response['answer'] = 'Вопрос сохранен в облаке'

    putObject(bucket_name, key_path, json.dumps(dataList))
    response['data'] = 'Вопросов в облаке: ' + str(len(dataList))
    response['result'] = True
    
    return {
        'statusCode': 200,
        'headers': {
                #Если закоментить headers: 
                #Request header field content-type is not allowed by Access-Control-Allow-Headers in preflight response
                "Access-Control-Allow-Headers": "Content-Type", 
                "Content-Type": "application/json; charset=utf-8",
                #"Accept-Post": "application/json; charset=utf-8"
            },
        
         'body': json.dumps(
            response, 
            default=vars,
         ),
    }
