from flask import Flask, render_template ,request, render_template
from flask_cors import cross_origin
import deepface as DeepFace
from expression import expressions
from face_detect import facess
import json
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/emotions", methods=["GET", "POST"])
@cross_origin()
def emotions():
    if request.method == "POST":
        video_rec = expressions()
        with open("data.json", "r") as f:
            emotionss = json.load(f)
            
            angry_value = emotionss[0]["angry"]
            sad_value = emotionss[0]["sad"]
            neutral_value = emotionss[0]["neutral"]
            
        return render_template('index.html',result = video_rec, Card_1="{}".format(angry_value),Card_2="{}".format(sad_value),Card_3="{}".format(neutral_value))
    return render_template("index.html")

@app.route("/face", methods=["GET", "POST"])
@cross_origin()
def face():
    if request.method == "POST":
        facee = facess()
                    
        return render_template("index.html",result = facee)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
