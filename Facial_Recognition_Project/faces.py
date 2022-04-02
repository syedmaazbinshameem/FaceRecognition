from cProfile import label
from tkinter import Frame
import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    oglabels = pickle.load(f)
    labels = {v:k for k,v in oglabels.items()}

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame by frame
    ret, Frame = cap.read()

    # Convert to Grayscale
    gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

    # Detects frontal face using face cascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x, y, w, h) in faces:
        #print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+h]
        roi_color = Frame[y:y+h, x:x+h]

        # Recognizer
        id_, conf = recognizer.predict(roi_gray)
        if conf >= 40:
            #print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(Frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

        img_item = 'my-image.png'
        cv2.imwrite(img_item, roi_gray)

        # Rectangle features
        color = (255, 0, 0)
        stroke = 2
        
        # Ending co-ordinates of x and y of the rectangle
        width = x + w
        height = y + h
        cv2.rectangle(Frame, (x, y), (width, height), color, stroke)
    # Display the resulting frame
    cv2.imshow('frame',Frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()