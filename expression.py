import cv2
import numpy as np
from deepface import DeepFace
import cv2
import time
import json

def expressions():
    # Load the cascade classifier
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Load the video
    cap = cv2.VideoCapture("head.mp4")
    emotions = []
    time = 1
    while time != 20:
        # Capture a frame from the video
        ret, frame = cap.read()


        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Loop over the faces
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]

            # Predict the emotion of the face
            emotion = DeepFace.analyze(face_img, actions = ['emotion'],enforce_detection=False)
            # Draw the predicted emotion on the frame
            emotions.append(emotion)
            angry_data = [data['emotion'] for data in emotion]

            time += 1
            break

    # Release the video capture
    cap.release()
    with open('data.json', 'w') as f:
        json.dump(angry_data, f)
