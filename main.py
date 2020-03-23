from flask import Flask, escape, request, render_template
from word_dictionaries import WordDictionaries
from config.config import Config
from games import Games
import json

app = Flask(__name__)

WordDictionaries.initialize()
Config.initialize()

games = Games()


@app.route('/')
def main_path():
    name = request.args.get("name", "World")
    return "hello"

@app.route('/game_state', methods=['GET'])
def game_state():
    game_key = request.args.get("game_key")
    return json.dumps(games.get_game_state_dict(game_key))

@app.route('/create_game', methods=['POST'])
def create_game():

    data = request.form.to_dict()

    if len(data) > 0:
        data['red_players'] = [x.strip() for x in data['red_players'].split(',')]
        data['blue_players'] = [x.strip() for x in data['blue_players'].split(',')]
        return json.dumps(games.create(data))

    raise Exception('Invalid data')

@app.route('/pages/create')
def create_html():
    return render_template('create.html')

@app.route('/pages/game')
def game_html():
    return render_template('game.html')
