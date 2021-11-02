from student_identification.detectText import detect_text
from student_identification.compareFace import compare_faces
#from hand_detection.yolo3.src.yolo3_simple import YOLO
from hand_detection.google.google_hand import google_hands
from flask import Flask, redirect, url_for, request, render_template
# from flask_restful import reqparse
from flask_cors import CORS
from flask_restx import Resource, Api, fields, reqparse
# from keras import backend as K
import sys
sys.path.extend(["./","../"])
from PIL import Image
import json
import os

import s3path
import numpy as np
import cv2


app = Flask(__name__)
app.config.SWAGGER_UI_DOC_EXPANSION = 'full'

api = Api(app,versison='1.0',title='test-helper-ai-api',
          description = 'check test-helper-ai-api')
ns_identification = api.namespace('identification', description = 'student identification')

parser_identification = reqparse.RequestParser()
parser_identification.add_argument('test_id', type= str,help = 'ID of test',location='form')
parser_identification.add_argument('student_num', type= str,help = 'num of student',location='form')

@ns_identification.route("")
class Identification(Resource):
    @api.expect(parser_identification)
    def post(self):
        args = parser_identification.parse_args()

        test_id = args['test_id']
        student_num = args['student_num']

        if not test_id or not student_num :
            sys.stderr.write("no test_id or student_num in request body\n")
            return {'result' : False,
                            'err_reason' : 'check_request'}

        idcard_path= s3path.S3_ROOT+ test_id + s3path.S3_STUDENT_FOLDER+ student_num + s3path.S3_STUDENT_CARD
        face_path = s3path.S3_ROOT+ test_id + s3path.S3_STUDENT_FOLDER+ student_num + s3path.S3_FACE
        bucket=s3path.S3_BUCKET
        sys.stderr.write("idcard_path : {idcard_path}\n".format(idcard_path=idcard_path))
        sys.stderr.write("face_path : {face_path}\n".format(face_path=face_path))

        result_text = detect_text(bucket, idcard_path,student_num)
        if not result_text :
            sys.stderr.write("Real student num and student number in id_card do not match!\n")
            return {'result': False,
                               'err_reason' : 'student_num'}
    
        result_face = compare_faces(bucket,idcard_path,face_path)
        if not result_face :
            sys.stderr.write("Real student face and student image in id_card do not match!\n")
            return {'result': False,
                               'err_reason' : 'face'}
        return {'result' : result_face,
                           'err_reason': None }



# @app.route('/identification',methods=['POST'])
# def identification():
#     parser = reqparse.RequestParser()
#     parser.add_argument('test_id')
#     parser.add_argument('student_num')
    # args = parser.parse_args()

    # test_id = args['test_id']
    # student_num = args['student_num']
    
#     if not test_id or not student_num :
#         sys.stderr.write("no test_id or student_num in request body\n")
#         return json.dumps({'result' : False,
#                             'err_reason' : 'check_request'})

#     idcard_path= s3path.S3_ROOT+ test_id + s3path.S3_STUDENT_FOLDER+ student_num + s3path.S3_STUDENT_CARD
#     face_path = s3path.S3_ROOT+ test_id + s3path.S3_STUDENT_FOLDER+ student_num + s3path.S3_FACE
#     bucket=s3path.S3_BUCKET
#     sys.stderr.write("idcard_path : {idcard_path}\n".format(idcard_path=idcard_path))
#     sys.stderr.write("face_path : {face_path}\n".format(face_path=face_path))

#     result_text = detect_text(bucket, idcard_path,student_num)
#     if not result_text :
#         sys.stderr.write("Real student num and student number in id_card do not match!\n")
#         return json.dumps({'result': False,
#                            'err_reason' : 'student_num'})
    
#     result_face = compare_faces(bucket,idcard_path,face_path)
#     if not result_face :
#         sys.stderr.write("Real student face and student image in id_card do not match!\n")
#         return json.dumps({'result': False,
#                            'err_reason' : 'face'})
#     return json.dumps({'result' : result_face,
#                        'err_reason': None })



@app.route('/hand-detection',methods=['POST'])
def detection():
    sys.stderr.write(str(request.files['hand_img']))
    image = Image.open(request.files['hand_img'])
    hand_num = google_hands(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))
    # hand_num = yolo.detect_image(image)
    result=False
    if hand_num == 2 :
        result = True
   
    # K.clear_session()
    return json.dumps({'result':result})


if __name__ == '__main__':
    # model_path = "hand_detection/yolo3/model_data/custom_weights_final.h5"
    # class_path = "hand_detection/yolo3/model_data/classes.txt"
    # anchor_path = "hand_detection/yolo3/model_data/tiny_yolo_anchor.txt"
    # yolo = YOLO(model_path=model_path, classes_path=class_path, anchors_path=anchor_path)
    app.run(host='0.0.0.0',port=5000,threaded=True,debug=True)
    #app.run(host='0.0.0.0',port=5000,debug=True)