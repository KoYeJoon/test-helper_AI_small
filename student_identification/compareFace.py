import boto3
import json
import os
from dotenv import load_dotenv
load_dotenv()

def compare_faces(src_path,tar_path,bucket):
    client=boto3.client('rekognition')
    
    SIMILARITY_THRESHOLD = 75
    src_img = {'S3Object':{'Bucket':bucket,'Name': src_path}}
    tar_img = {'S3Object':{'Bucket':bucket,'Name': tar_path}}
    response = client.compare_faces(SimilarityThreshold=SIMILARITY_THRESHOLD, SourceImage=src_img, TargetImage=tar_img)

    # print(json.dumps(response, indent=4, sort_keys=True))
    if len(response['FaceMatches'])==0 :
        return False

    return True
    
def main():
    src_path = os.environ['S3_ROOT'] + os.environ['S3_TEMP_TEST'] + "/student/" + os.environ['S3_TEMP_STUDENT'] + "/id_card.jpg"
    tar_path = os.environ['S3_ROOT'] + os.environ['S3_TEMP_TEST'] + "/student/" + os.environ['S3_TEMP_STUDENT'] + "/face.jpg"
    # tar_path = os.environ['S3_ROOT'] + os.environ['S3_TEMP_TEST'] + "/student/" + os.environ['S3_TEMP_STUDENT'] + "/fake_face.jpg"
    bucket=os.environ['S3_BUCKET']
    response =compare_faces(src_path,tar_path, bucket)
    if response :
        print("Result : True")
    else :
        print("Result : False")


if __name__ == "__main__":
    main()

