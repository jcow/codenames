
import random
from config.config import Config

class URLMaker:

    FILEPATH_ADJECTIVES = "dictionaries/adjectives.txt"
    FILEPATH_ANIMALS = "dictionaries/animals.txt"

    def __init__(self):
        self.adjectives = []
        self.animals = []
        self._read_files()

    def make_game_key(self):
        return self.get_segments_and_concat()

    def get_url(self, game_key):
        host = Config.get_key("host")
        port = Config.get_key("port")

        url = ""
        url += host
        if port is not None and len(port) > 0:
            url += ":" + port

        url += "/game"

        url += "/" + game_key
        url += "/" + self.get_segments_and_concat()

        return url

    def get_segments_and_concat(self):
        return "".join(self.get_segments())

    def get_segments(self):
        url_a = random.choice(self.adjectives)
        url_b = self.get_unique(url_a, self.adjectives)
        url_c = random.choice(self.animals)

        return url_a, url_b, url_c

    def get_unique(self, previous_item, dictionary):
        found = False
        while found is False:
            item = random.choice(dictionary)
            if item != previous_item:
                return item

    def _read_files(self):
        with open(URLMaker.FILEPATH_ADJECTIVES) as f:
            for line in f:
                line = line.strip()
                if len(line) > 0:
                    self.adjectives.append(line)

        with open(URLMaker.FILEPATH_ANIMALS) as f:
            for line in f:
                line = line.strip()
                if len(line) > 0:
                    self.animals.append(line)
