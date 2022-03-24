import boto3
import os

try:
    with open('new_user_credentials.csv', 'r') as file:
        file.readline()
        creds_parts = file.readline().split(",")

    ACCESS_KEY = creds_parts[2]
    SECRET_ACCESS_KEY = creds_parts[3]
except:
    ACCESS_KEY = os.environ.get("USER_CREDENTIALS_USR")
    SECRET_ACCESS_KEY = os.environ.get("USER_CREDENTIALS_PSW")

BUCKET_NAME = 'jsolano.jenkinstest.s3'

s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY
)

bucket = s3.list_objects(Bucket=BUCKET_NAME)

for file in bucket['Contents']:
    name = file['Key']
    print("Downloading file: {0}".format(name))
    s3.download_file(BUCKET_NAME, name, 'res/{0}'.format(name))
