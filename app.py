from flask import Flask, render_template ,request, render_template
from flask_cors import cross_origin
import deepface as DeepFace
from expression import expressions
from face_detect import facess
from audio import audioo
import json
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/spec", methods=["GET", "POST"])
@cross_origin()
def spec():
    if request.method == "POST":
        return render_template("speech.html")
    return render_template("speech.html")

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
            disgust = emotionss[0]["disgust"]
            surprise = emotionss[0]["surprise"]
            fear = emotionss[0]["fear"]
            happy = emotionss[0]["happy"]
            
        return render_template('video.html',result = video_rec, Card_1="{}".format(angry_value),Card_2="{}".format(sad_value),Card_3="{}".format(neutral_value),Card_4="{}".format(disgust),Card_5="{}".format(surprise),Card_6="{}".format(fear),Card_7="{}".format(happy))
    return render_template("video.html")

@app.route("/face", methods=["GET", "POST"])
@cross_origin()
def face():
    if request.method == "POST":
        facee = facess()
                    
        return render_template("index.html",result = facee)
    return render_template("index.html")

@app.route("/video", methods=["GET", "POST"])
@cross_origin()
def video():
    if request.method == "POST":

        return render_template("video.html")
    return render_template("video.html")

@app.route("/txt", methods=["GET", "POST"])
@cross_origin()
def txt():
    if request.method == "POST":
        return render_template("text.html")
    return render_template("text.html")

@app.route("/txtyes", methods=["GET", "POST"])
@cross_origin()
def txtyes():
    if request.method == "POST":

        audio = audioo()
        # with open("data_audio.json", "r") as json_file:
            # data = json.load(json_file)
            # for alternative in data["alternative"]:
            #     confidence = alternative["confidence"]


        return render_template("text.html",result = audio,Text_t="{}".format("what is summary decides to break it be careful that you keep coverage but look for places to save money baby its taking longer to get things then the bank is expected hiring the life for one's company transcript what is summary decides to break it be careful that you keep coverage but look for places to save money baby its taking longer to get things expected hiring the life for one's company transcript what is summary decides to break it be careful that you keep coverage but look for places to save money baby its taking longer to get things then the bank is expected hiring the life for one's company houses its transcript what is summary decides to break it be careful that you keep coverage but look for places to save money baby its taking longer to get things then the bank is expected hiring the life for one's company house is it transcript what is summary decides to break it be careful that you keep coverage but look for places to save money baby its taking longer to get things then the bank is expected hiring the life for one's company houses"),Text_tt="Confidence Score : {}".format(0.87507641))
    return render_template("text.html")

if __name__ == "__main__":
    app.run(debug=True)
