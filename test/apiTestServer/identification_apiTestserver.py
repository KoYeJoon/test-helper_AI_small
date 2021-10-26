import unittest
import os
import warnings
import json
import requests 

from dotenv import load_dotenv
load_dotenv()


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.host = 'http://localhost:5000'
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
        response = requests.post(self.host+'/identification', data=self.right_parameter)
        data = response.json()
        self.assertEqual(True, data['result'])


    def test_wrong_test_parameter(self):
        response = requests.post(self.host+"/identification",data=self.wrong_parameter_testID)
        data = response.json()
        self.assertEqual(False,data['result'])

    def test_wrong_studentID_parameter(self):
        response = requests.post(self.host+"/identification",data=self.wrong_parameter_studentID)
        data = response.json()
        self.assertEqual(False,data['result'])

    def test_no_test_parameter(self):
        response = requests.post(self.host+"/identification",data=self.no_parameter_testID)
        data = response.json()
        self.assertEqual(False,data['result'])

    def test_no_studentID_parameter(self):
        response = requests.post(self.host+"/identification",data=self.no_parameter_studentID)
        data = response.json()
        self.assertEqual(False,data['result'])

if __name__ == "__main__":
    unittest.main()