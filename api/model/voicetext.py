import json
import requests
from requests.auth import HTTPBasicAuth

class VoiceText:
    VERSION = "v1"
    ENDPOINT = "https://api.voicetext.jp/%s/tts" % VERSION

    def __init__(self, api_key):
        self.api_key = api_key

    def generate(self, text, speaker, speed = 100, pitch = 100, volume = 100, emotion=None, emotion_level = 2):
        params = {
            "text": text,
            "speaker": speaker,
            "speed": speed,
            "pitch": pitch,
            "volume": volume,
        }

        if emotion:
            params["emotion"] = emotion
            params["emotion_level"] = emotion_level

        data = self._request(params)

        return data

    def _request(self, params):
        auth = HTTPBasicAuth(self.api_key, "")
        res = requests.post(self.ENDPOINT, params=params, auth=auth)

        if res.status_code == 200:
            return res.content
        else:
            content = json.loads(res.content)
            message = content["error"]["message"]
            raise Exception("%s: %s" % (res.status_code, message))

