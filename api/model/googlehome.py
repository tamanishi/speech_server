import time

import pychromecast

class GoogleHome:
    def __init__(self, friendly_names):
        self.friendly_names = friendly_names

    def play(self, url):
        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=self.friendly_names)

        cast = chromecasts[0]
        cast.wait()

        cast.media_controller.play_media(self._add_ts_to(url), "audio/wav")
        browser.stop_discovery()

    def _add_ts_to(self, url):
        return url + '?ts={}'.format(int(time.time()))
