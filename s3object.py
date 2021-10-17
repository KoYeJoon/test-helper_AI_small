# import boto3

# BUCKET_NAME = 'mybucket'
# client = boto3.client('s3')
# response = client.list_objects(Bucket=BUCKET_NAME)

# for content in response['Contents']:
#     obj_dict = client.get_object(Bucket=BUCKET_NAME, Key=content['Key'])
#     print(content['Key'], obj_dict['LastModified'])

import logging
import boto3
from botocore.exceptions import BotoCoreError
from contextlib import closing

import os
from dotenv import load_dotenv
load_dotenv()

def handle_upload_img(file_name, bucket, object_name=None): 
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = 'image/'+os.path.basename(file_name)
    response = s3_client.upload_file(file_name,bucket,object_name)
   

handle_upload_img('images/hand2.jpg',os.environ['S3_BUCKET'])