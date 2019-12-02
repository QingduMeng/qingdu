import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAJAPEXNWMM3X7RTRA'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'rbiqingdumeng'

# upload a file
data = open('S3(1).py', 'rb')
s3 = boto3.resource(
    's3',
    aws_access_key_id = ACCESS_KEY_ID,
    aws_secret_access_key = ACCESS_SECRET_KEY,
    config = Config(signature_version = 's3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='S3(1).py', Body=data)

# download a file
KEY = 'S3(1).py'
s3.Bucket(BUCKET_NAME).download_file(KEY, 'rbi.py')

# download all files
s3 = boto3.client(
    's3',
    aws_access_key_id = ACCESS_KEY_ID,
    aws_secret_access_key = ACCESS_SECRET_KEY,
    config = Config(signature_version = 's3v4')
)
list=s3.list_objects(Bucket='rbiqingdumeng')['Contents']
for key in list:
    s3.download_file('rbiqingdumeng', key['Key'], key['Key'])

print('Done')


