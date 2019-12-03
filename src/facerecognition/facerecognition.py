import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")

img = cv2.imread("image4.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imwrite("test.png", img)
