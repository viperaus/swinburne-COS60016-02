from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter, BestMatch, TimeLogicAdapter
from ChatterbotAdapters.weather import WeatherInCityAdapter
import logging


logging.basicConfig(level=logging.INFO)
custom_logger = logging.getLogger(__name__)

app = Flask(__name__)

chatbot = ChatBot('Ronnie',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter', 
                  preprocessors=['chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.unescape_html','chatterbot.preprocessors.convert_to_ascii'],
                  database_uri='sqlite:///db.sqlite3',
                  read_only=True,
                  logger=custom_logger)

chatbot.logic_adapters.append(WeatherInCityAdapter(chatbot))
chatbot.logic_adapters.append(BestMatch(chatbot, excluded_words=["time"]))
chatbot.logic_adapters.append(TimeLogicAdapter(chatbot))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('question')
    return str(chatbot.get_response(user_input))


if __name__ == "__main__":
    app.run()