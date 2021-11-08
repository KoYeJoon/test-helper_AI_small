#!bin/bash
#api Test
echo API TEST
python test/apiTest/identification_apiTest.py
echo "\n"
python test/apiTest/hand_detection_apiTest.py

echo "\n\n\n"
echo MODULE TEST
python test/moduleTest/hand_detection_moduleTest.py
echo "\n"
python test/moduleTest/identification_moduleTest.py
