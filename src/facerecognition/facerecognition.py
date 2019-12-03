import cv2
import numpy as np

# carga archivo Haar Cascade para reconocimiento de rostros
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")

# lee imagen desde el disco duro
img = cv2.imread("image.jpg")
# la convierte a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecta los rostros
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# itera en los rostros detectados
for (x, y, w, h) in faces:
    # traza las ubicaciones de los pixeles de los rostros
    roi_color = img[y:y + h, x:x + w]

    # escribe un archivo por cada rostro
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)

    # dibuja un rectangulo en cada rostro
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# escribe un archivo con rectángulos en cada rostro
cv2.imwrite("image_test.png", img)
