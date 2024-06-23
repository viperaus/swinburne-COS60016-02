venv/scripts/activate: requirements.txt
		py -3.7 -m venv .venv
		./.venv/scripts/pip install -r requirements.txt

setup: venv/scripts/activate
		./.venv/scripts/python scaffold_db.py
		make train

run: venv/scripts/activate
		./.venv/scripts/python app.py

train: venv/scripts/activate
		./.venv/scripts/python train_chatbot.py

clean-training:
		rm -rf ./db.sqlite3
		rm -rf ./.training_completed
		rm -rf ./sentence_tokenizer.pickle

clean:
		rm -rf ./__pycache__
		rm -rf ./ChatterbotAdapters/__pycache__
		rm -rf ./.venv