# Swinburne COS60016 Assignment 2

## Instructions

1. Ensure you have Python 3.7 installed on your machine - this project will not work with other versions of Python.

2. Clone this repository to your local machine.

```
git clone https://github.com/viperaus/swinburne-COS60016-02.git
```

3. Enter the project directory 

```
cd swinburne-COS60016-02
```

4. Rename the `.env.example` file to `.env` and update the values as required.

5. Run the following command to install the required packages

```
make setup
```

4. Once the setup is complete, run the following command to start the server

```
make run
```

5. Open a browser and navigate to `http://localhost:5000` or if your server is running on a different port, navigate to `http://localhost:<port>`.

## Creating custom training data

The training data is stored in the `training_data` directory. There are two types of files in this directory:

- `*.txt`: These are the conversations that will be used to train the model. Each conversation is stored in a separate file.
- `*.yml`: These are corpus files

