import os
from flask import Blueprint, request

from ..model.voicetext import VoiceText
from ..model.googlehome import GoogleHome

app = Blueprint("speech", __name__, url_prefix="/speech")

@app.route("/", methods=["POST"])
def speech():

    voicetext = VoiceText(os.getenv("VOICETEXT_APIKEY"))

    data = voicetext.generate(request.json["text"], request.json["speaker"], request.json["speed"], request.json["pitch"], volume = None, emotion = request.json["emotion"], emotion_level = request.json["emotion_level"])

    AUDIO_FILE = "out.wav"
    _save(data, AUDIO_FILE)

    url = _deriveurl(AUDIO_FILE)

    googlehome = GoogleHome([os.getenv("CAST_NAME")])
    googlehome.play(url)

    return "", 200

def _save(data, filename):
    with open("static/" + filename, "wb") as f:
        f.write(data)

def _deriveurl(filename):
    return os.getenv("SERVERURL") + filename
