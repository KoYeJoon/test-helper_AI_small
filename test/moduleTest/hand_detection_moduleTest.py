import unittest
import cv2
import sys
sys.path.extend(["./src","../src","../../src"])
from hand_detection.google.google_hand import google_hands

class UnitTest(unittest.TestCase):
    def setUp(self): 
        self.fourhands = cv2.imread("test/hands/fourhands.jpg")
        self.twohands = cv2.imread("test/hands/twohands.jpg")
        self.onehand = cv2.imread("test/hands/onehand.jpg")

    def test_four_hands(self):
        self.assertEqual(4,google_hands(self.fourhands))

    def test_two_hands(self):
        self.assertEqual(2,google_hands(self.twohands))

    def test_one_hand(self):
        self.assertEqual(1,google_hands(self.onehand))


if __name__ == '__main__':
    unittest.main()