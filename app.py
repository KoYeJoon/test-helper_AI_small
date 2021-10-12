import requests
import os
import uuid
import json

from detectText import detect_text
from compareFace import compare_faces
# from keras.models import load_model
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/temp/identification',methods=['POST'])
def identification():
    test_id = request.form['test_id']
    student_id = request.form['student_id']
    idcard_path=os.environ['S3_ROOT'] + test_id + "/student/" + student_id + "/id_card.jpg"
    bucket=os.environ['S3_BUCKET']
    result_text = detect_text(idcard_path, bucket,student_id)

    if not result_text :
        return render_template(
            'result_id.html',
            result = result_text,
        )
        # return {'result': False}

    face_path = os.environ['S3_ROOT'] + test_id + "/student/" + student_id + "/face.jpg"
    result_face =compare_faces(idcard_path,face_path, bucket)

    return render_template(
            'result_id.html',
            result = result_face,
        )
    # return {'result' : result_face}


@app.route('/temp/detection',methods=['POST'])
def detection():
    pass


# @app.route('/identification/face',method=['POST'])
# def identification():
#     pass

# @app.route('/tests/{testID}/detection',method=['POST'])
# def detection():
#     pass



if __name__ == '__main__':
    # model = load_model('./hand_detection/model.h5')
    app.run(host='0.0.0.0',port=5000,debug=True)