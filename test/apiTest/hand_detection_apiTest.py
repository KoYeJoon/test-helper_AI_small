import unittest
import json
from io import BytesIO
import sys

sys.path.extend(["./","../","../../","./src","../src","../../src","./test"])
import app

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        with open("test/hands/onehand.jpg", 'rb') as img1:
            self.onehand = BytesIO(img1.read())
        with open("test/hands/twohands.jpg", 'rb') as img2:
            self.twohand = BytesIO(img2.read())
        with open("test/hands/fourhands.jpg", 'rb') as img3:
            self.fourhand = BytesIO(img3.read())
        self.wrong = "wrong"

        self.onehand_parameter = {
            'hand_img' : (self.onehand, 'img.jpg')
        }
        self.twohand_parameter = {
            'hand_img' : (self.twohand, 'img.jpg')
        }
        self.fourhand_parameter= {
            'hand_img' : (self.fourhand, 'img.jpg')
        }
        self.wrong_parameter={
            'hand_img' : self.wrong
        }
        self.no_parameter = {
            'hand_img' : None
        }

    def test_onehand_parameter(self):
        response = self.app.post('/hand-detection', data=self.onehand_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False, data['result'])

    def test_twohand_parameter(self):
        response = self.app.post('/hand-detection', data=self.twohand_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(True, data['result'])

    def test_fourhand_parameter(self):
        response = self.app.post('/hand-detection', data=self.fourhand_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False, data['result'])

    def test_wrong_parameter(self):
        response = self.app.post('/hand-detection', data=self.wrong_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False, data['result'])

    def test_no_parameter(self):
        response = self.app.post('/hand-detection', data=self.no_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False, data['result'])

if __name__ == "__main__":
    unittest.main()