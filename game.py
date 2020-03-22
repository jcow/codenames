
from player import Player
from color import Color
from url_maker import URLMaker
from config.config import Config


class Game:

    url_maker = URLMaker()

    def __init__(self):

        self.red_players = set()
        self.blue_players = set()

        self.red_spymaster = None
        self.blue_spymaster = None

        game_key = self.url_maker.make_game_key()

        self.game_key = game_key
        self.red_spymaster_url = self.url_maker.get_url(game_key)
        self.blue_spymaster_url = self.url_maker.get_url(game_key)
        self.red_url = self.url_maker.get_url(game_key)
        self.blue_url = self.url_maker.get_url(game_key)

    def get_game_key(self):
        return self.game_key

    def get_red_players(self):
        return self.red_players

    def get_blue_players(self):
        return self.blue_players

    def get_red_spymaster(self):
        return self.red_spymaster

    def get_blue_spymaster(self):
        return self.blue_spymaster

    def get_red_spymaster_url(self):
        return self.red_spymaster_url

    def get_blue_spymaster_url(self):
        return self.blue_spymaster_url

    def get_red_url(self):
        return self.red_url

    def get_blue_url(self):
        return self.blue_url

    def is_valid_game(self):
        if self.red_spymaster is None:
            raise Exception("red spymaster not specified")

        if self.blue_spymaster is None:
            raise Exception("blue spymaster is not specified")

        if self.red_players is None:
            raise Exception("There are no red players")

        if self.blue_players is None:
            raise Exception("There are no blue players")

    def add_spymaster(self, name, color):
        if self._is_color_red(color):
            self.red_spymaster = Player(name)
        elif self._is_color_blue(color):
            self.blue_spymaster = Player(name)
        else:
            raise ValueError('Wrong color specified')

    def add_player(self, name, color):
        if self._is_color_red(color):
            self._add_player(self.red_players, name)
        elif self._is_color_blue(color):
            self._add_player(self.blue_players, name)
        else:
            raise ValueError('Wrong color specified')

    def remove_player(self, name, color):
        if self._is_color_red(color):
            self._remove_player(self.red_players, name)
        elif self._is_color_blue(color):
            self._remove_player(self.blue_players, name)
        else:
            raise ValueError('Wrong color specified')

    def _is_color_red(self, color):
        return color == Color.RED

    def _is_color_blue(self, color):
        return color == Color.BLUE

    def _add_player(self, color_set, name):
        if name in color_set:
            raise ValueError('Player already in game')

        color_set.add(Player(name))

    def _remove_player(self, color_set, name):
        if name in color_set:
            color_set.remove(Player(name))
        else:
            raise ValueError("Player doesn't exist")
