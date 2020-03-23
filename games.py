
from color import Color
from game import Game
import json

class Games:

    games = {}

    def create(self, json_data):

        red_spymaster = None
        if 'red_spymaster' in json_data:
            red_spymaster = json_data['red_spymaster']

        blue_spymaster = None
        if 'blue_spymaster' in json_data:
            blue_spymaster = json_data['blue_spymaster']

        red_players = []
        if 'red_players' in json_data:
            red_players = json_data['red_players']

        blue_players = []
        if 'blue_players' in json_data:
            blue_players = json_data['blue_players']

        game = Game()

        game.add_spymaster(red_spymaster, Color.RED)
        game.add_spymaster(blue_spymaster, Color.BLUE)

        for red_person in red_players:
            game.add_player(red_person, Color.RED)

        for blue_person in blue_players:
            game.add_player(blue_person, Color.BLUE)

        if game.is_valid_game() is False:
            raise Exception("Invalid game state " + game.__dict__)

        self.games[game.get_game_key()] = game

        game_state = self.get_game_state_dict(game.get_game_key())

        return game_state

    def get_game_state_dict(self, game_key):
        if game_key not in self.games:
            raise Exception("Gamekey not in games " + game_key)

        game = self.games[game_key]

        d = {}
        d['game_key'] = game.get_game_key()
        d['red_spymaster'] = game.get_red_spymaster().get_name()
        d['red_spymaster_url'] = game.get_red_spymaster_url()
        d['red_players'] = list([x.get_name() for x in game.get_red_players()])
        d['red_players_url'] = game.get_red_url()
        d['blue_spymaster'] = game.get_blue_spymaster().get_name()
        d['blue_spymaster_url'] = game.get_blue_spymaster_url()
        d['blue_players'] = list([x.get_name() for x in game.get_blue_players()])
        d['blue_players_url'] = game.get_blue_url()

        return d
