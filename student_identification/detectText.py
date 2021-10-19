import boto3
import json
import os
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
        print("AWS 에 접근 시 오류가 발생하였습니다! ")
        return False

    return correct
    
def main():
    path=os.environ['S3_ROOT'] + os.environ['S3_TEMP_TEST'] + "/submission/" + os.environ['S3_TEMP_STUDENT'] + "/student_card.jpg"
    bucket=os.environ['S3_BUCKET']
    student_id=os.environ['STUDENT_ID']
    response =detect_text(bucket, path, student_id)
    if response :
        print("Result : True")
    else :
        print("Result : False")


if __name__ == "__main__":
    main()

