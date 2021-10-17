import sys
sys.path.append("..")

from student_identification.detectText import detect_text
from student_identification.compareFace import compare_faces
from hand_detection.yolo3.src.yolo3_cv import YOLO

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, redirect, url_for, request, render_template, send_file
from flask_cors import CORS
from keras import backend as K


from PIL import Image
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def index_test():
    return render_template('index.html')


@app.route('/identification',methods=['POST'])
def identification_test():
    test_id = request.form['test_id']
    student_id = request.form['student_id']
    idcard_path=os.environ['S3_ROOT'] + test_id + "/submission/" + student_id + "/student_card.jpg"
    bucket=os.environ['S3_BUCKET']
    result_text = detect_text(bucket, idcard_path,student_id)

    if not result_text :
        return render_template(
            'result_id.html',
            result = result_text,
        )

    face_path = os.environ['S3_ROOT'] + test_id + "/submission/" + student_id + "/face.jpg"
    result_face =compare_faces(bucket,idcard_path,face_path)

    return render_template(
            'result_id.html',
            result = result_face,
        )


@app.route('/hand-detection',methods=['POST'])
def temp_detection_test():
    # model = yolo.get_model()
    # model.summary()
    
    image = Image.open(request.files['hand_img'])
    print(yolo)
    result_image,hand_num,bbox = yolo.detect_image(image)
    #opencvImage = cv2.cvtColor(np.array(result_image), cv2.COLOR_RGB2BGR) 
    #opencvImage = cv2.resize(opencvImage,dsize=(360,240))
    opencvImage = cv2.resize(result_image,dsize=(360,240))
    cv2.imwrite("static/images/result.jpg",opencvImage)
    result_path = "images/result.jpg"
    # K.clear_session()
    return render_template(
            'result_hand.html', 
            result_path = result_path,
            hand_num=hand_num, bbox=bbox
    )


if __name__ == '__main__':
    model_path = "../hand_detection/yolo3/model_data/custom_weights_final.h5"
    class_path = "../hand_detection/yolo3/model_data/classes.txt"
    anchor_path = "../hand_detection/yolo3/model_data/tiny_yolo_anchor.txt"
    yolo = YOLO(model_path=model_path, classes_path=class_path, anchors_path=anchor_path)
    app.run(host='0.0.0.0',port=5000,threaded=True, debug=True)
    #app.run(host='0.0.0.0',port=5000,debug=True)