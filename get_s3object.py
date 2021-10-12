import boto3

BUCKET_NAME = 'mybucket'
client = boto3.client('s3')
response = client.list_objects(Bucket=BUCKET_NAME)

for content in response['Contents']:
    obj_dict = client.get_object(Bucket=BUCKET_NAME, Key=content['Key'])
    print(content['Key'], obj_dict['LastModified'])