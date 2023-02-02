import cv2
import numpy as np
from keras.models import load_model

def facess():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    model = load_model("emotion_little_vgg_3.h5")

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:

            face_region = gray[y:y+h, x:x+w]

    
            face_region = cv2.resize(face_region, (48, 48))

            face_region = np.expand_dims(face_region, axis=0)
            face_region = np.expand_dims(face_region, axis=-1)

            prediction = model.predict(face_region)

    
            expression = np.argmax(prediction)

        
            expression_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Confident", "Neutral"]
            expression_label = expression_labels[expression]

        
            cv2.putText(frame, expression_label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1)

    
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 1)


        cv2.imshow("frame", frame)

        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()
