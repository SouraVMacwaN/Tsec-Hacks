import speech_recognition as sr
import json
def audioo():
    r = sr.Recognizer()
    with sr.AudioFile("./videos/male.wav") as source:
        audio = r.record(source)
    # from pydub import AudioSegment


    # # Load audio file
    # audio = AudioSegment.from_file("input.mp3")

    # # Split audio every 10 seconds
    # ten_seconds = 10 * 1000
    # for i in range(0, len(audio), ten_seconds):
    #     audio_part = audio[i:i+ten_seconds]
    #     audio_part.export("part_{}.mp3".format(i), format="mp3")
    # Perform speech-to-text recognition


    text = r.recognize_google(audio,show_all=True)

    with open('data_audio.json', 'w') as f:
            json.dump(text, f)
    

