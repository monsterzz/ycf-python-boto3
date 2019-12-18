import boto3
import os


s3 = boto3.client('s3', endpoint_url='https://storage.yandexcloud.net/')
bucket_name = os.environ['STORAGE_BUCKET']
object_name = 'function-test.txt'


def put_object():
    data = open('/proc/uptime', 'rb').read()
    s3.put_object(Bucket=bucket_name, Key=object_name, Body=data)


def get_object_mtime():
    obj = s3.get_object(Bucket=bucket_name, Key=object_name)
    return str(obj['LastModified'])


def handler(event, context):
    put_object()
    return {
        'LastModified': get_object_mtime(),
    }
