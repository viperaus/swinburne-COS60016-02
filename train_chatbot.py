import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.logic import LogicAdapter, BestMatch, TimeLogicAdapter
import logging
from ChatterbotAdapters.weather import WeatherInCityAdapter

logging.basicConfig(level=logging.INFO)
custom_logger = logging.getLogger(__name__)

chatbot = ChatBot('Ronnie',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter', 
                  preprocessors=['chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.unescape_html','chatterbot.preprocessors.convert_to_ascii'],
                  database_uri='sqlite:///db.sqlite3',
                  read_only=True,
                  logger=custom_logger)

# add logic adapters
chatbot.logic_adapters.append(WeatherInCityAdapter(chatbot))
chatbot.logic_adapters.append(BestMatch(chatbot, excluded_words=["time"]))
chatbot.logic_adapters.append(TimeLogicAdapter(chatbot))

# check if training has been completed in the past
training_data_exists = os.path.exists('export.log')
if not training_data_exists:
    
    # initialize trainer
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english.botprofile")
    trainer.train("chatterbot.corpus.english.conversations")
    trainer.train("chatterbot.corpus.english.emotion")
    trainer.train("chatterbot.corpus.english.greetings")
    trainer.train("chatterbot.corpus.english.humor")
    
    # set training folder name
    directory = 'training_data'
    
    # loop through training folder
    for filename in os.listdir(directory):
        if filename.endswith(".txt"): # pick txt file for training as a conversation
            print('\n Chatbot training with '+os.path.join(directory, filename)+' file') # provide feedback to user
            training_data = open(os.path.join(directory, filename)).read().splitlines() # read txt file
            trainer = ListTrainer(chatbot) # reinitialize trainer
            trainer.train(training_data) # train conversation
        if filename.endswith(".yml"): # pick yml file for training as a corpus 
            print('\n Chatbot training with '+os.path.join(directory, filename)+' file') # provide feedback to user
            trainer = ChatterBotCorpusTrainer(chatbot) # reinitialize trainer
            trainer.train(directory+"."+filename.split(".")[0]) # train corpus
        else:
            continue # skip to next file

            continue


while True:
    try:
        request = input("You: ")
        if request.lower() == "bye":
            print("Goodbye!")
            raise SystemExit
        bot_response = chatbot.get_response(request)
        print(f"{chatbot.name}: {bot_response}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        print("Exiting...")
        trainer.export_for_training('export.log')
        break

