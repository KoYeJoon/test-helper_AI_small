import boto3
import json
import os
from dotenv import load_dotenv
load_dotenv()

def detect_text(photo, bucket,studentID):

    client=boto3.client('rekognition')

    response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    print('Detected texts for ' + photo)   
    correct = False 
    for textDetail in response['TextDetections']:
        # print(json.dumps(textDetail, indent=4, sort_keys=True))
        # print("DetectedText : " + str(textDetail['DetectedText']))
        # print("Confidence: " + str(textDetail['Type']))
        if studentID == str(textDetail['DetectedText']) :
            correct= True

    return correct
    
def main():
    photo=os.environ['S3_IMAGE']
    bucket=os.environ['S3_BUCKET']
    studentID=os.environ['STUDENT_ID']
    response =detect_text(photo, bucket,studentID)
    if response :
        print("Result : True")
    else :
        print("Result : False")


if __name__ == "__main__":
    main()

