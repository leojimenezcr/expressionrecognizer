#!/usr/bin/python3

import cv2

import facerecognition
import signrecognition
import postprocessing

# Capture a file (path) or webcam (id 0,1,...)
capture = cv2.VideoCapture(0)

while True:
    # 1. Video capture -> imgframe
    ret, imgframe = capture.read()

    # 2. imgframe -> facerecoginition -> return emotion label
    # 3. imgframe -> signrecogintion -> return sign label
    # 4. emotion label, sign label -> postprocessing -> return expression

    # Wait for a 'q' key
    cv2.imshow("Capture (key q for quit): ", imgframe)
    if cv2.waitKey(10) == ord('q'):
        break
