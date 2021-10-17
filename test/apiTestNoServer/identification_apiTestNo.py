from typing import Union
import unittest
import os
import warnings
import requests
import json

from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.append("../../")

import app

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.studentID = os.environ['S3_TEMP_STUDENT']
        self.testID = os.environ['S3_TEMP_TEST']
        self.fakestudentID = '00000000'
        self.faketestID = '000000'
        self.right_parameter = {
            'test_id' : self.testID,
            'student_id' : self.studentID
        }
        self.wrong_parameter_testID = {
            'test_id' : self.faketestID,
            'student_id' : self.studentID
        }
        self.wrong_parameter_studentID= {
            'test_id' : self.testID,
            'student_id' : self.fakestudentID
        }
        self.no_parameter_studentID={
            'test_id' : self.testID
        }
        self.no_parameter_testID = {
            'student_id' : self.studentID
        }
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>") 

    def test_right_parameter(self):
        response = self.app.post('/identification', data=self.right_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(True, data['result'])


    def test_wrong_test_parameter(self):
        response = self.app.post("/identification",data=self.wrong_parameter_testID)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False,data['result'])

    def test_wrong_studentID_parameter(self):
        response = self.app.post("/identification",data=self.wrong_parameter_studentID)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False,data['result'])

    def test_no_test_parameter(self):
        response = self.app.post("/identification",data=self.no_parameter_testID)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False,data['result'])

    def test_no_studentID_parameter(self):
        response = self.app.post("/identification",data=self.no_parameter_studentID)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False,data['result'])

if __name__ == "__main__":
    unittest.main()