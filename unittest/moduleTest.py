import unittest
import requests
import os
import warnings
from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.append("..")

from student_identification.compareFace import compare_faces
from student_identification.detectText import detect_text

    
class UnitTest(unittest.TestCase):
    def setUp(self):
        self.bucket = os.environ['S3_BUCKET']
        self.real_studentID = os.environ['S3_TEMP_STUDENT']
        self.fake_studentID = '201820000'
        self.src_real_path = os.environ['S3_ROOT'] + os.environ['S3_TEMP_TEST'] + "/submission/" + os.environ['S3_TEMP_STUDENT'] + "/student_card.jpg"
        self.tar_real_path = os.environ['S3_ROOT'] + os.environ['S3_TEMP_TEST'] + "/submission/" + os.environ['S3_TEMP_STUDENT'] + "/face.jpg"
        self.tar_fake_path = os.environ['S3_ROOT'] + os.environ['S3_TEMP_TEST'] + "/submission/" + os.environ['S3_TEMP_STUDENT'] + "/fake_face.jpg"
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>") 

    def tearDown(self):
        """테스트 종료 후 파일 삭제 """
        pass
       
    
    def test_wrong_face(self):
        self.assertEqual(False,compare_faces(self.bucket,self.src_real_path,self.tar_fake_path))

    def test_right_face(self):
        self.assertEqual(True,compare_faces(self.bucket,self.src_real_path,self.tar_real_path))

    
    def test_wrong_card(self):
        self.assertEqual(False,detect_text(self.bucket,self.src_real_path,self.fake_studentID))

    def test_right_card(self):
        self.assertEqual(True,detect_text(self.bucket,self.src_real_path,self.real_studentID))




if __name__ == '__main__':
    unittest.main()