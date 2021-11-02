import boto3
import json
import os
import sys
from dotenv import load_dotenv
load_dotenv()

def detect_text(bucket,path,studentID):
    image = {'S3Object':{'Bucket':bucket,'Name':path}}
    correct = False 
    try :
        client=boto3.client('rekognition')
        response = client.detect_text(Image=image)
        # print('Detected texts for ' + path)   
        for textDetail in response['TextDetections']:
            # print(json.dumps(textDetail, indent=4, sort_keys=True))
            # print("DetectedText : " + str(textDetail['DetectedText']))
            # print("Confidence: " + str(textDetail['Type']))
            if studentID == str(textDetail['DetectedText']) :
                correct= True
                break
    except:
        sys.stderr.write("AWS 에 접근 시 오류가 발생하였습니다! ")
        return False

    return correct
    
def main():
    sys.path.append('../')
    import s3path
    bucket=s3path.S3_BUCKET
    path=s3path.S3_ROOT + s3path.S3_TEMP_TEST_ID + s3path.S3_STUDENT_FOLDER+ s3path.S3_TEMP_STUDENT_NUM + s3path.S3_STUDENT_CARD
    student_num= s3path.S3_TEMP_STUDENT_NUM
    response =detect_text(bucket,path, student_num)
    if response :
        print("Result : True")
    else :
        print("Result : False")


if __name__ == "__main__":
    main()

