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



@app.route('/create_game', methods=['POST'])
def create_game():

    if 'data' in request.form:
        data = request.form['data']
        json_data = json.loads(data)

        return json.dumps(games.create(json_data))


    raise Exception('Invalid data')

@app.route('/pages/create')
def create_html():
    return render_template('create.html')
