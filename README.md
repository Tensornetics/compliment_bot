# ComplimentBot

ComplimentBot is a cloud-based software as a service (SaaS) that generates positive and encouraging compliments for users.

## Prerequisites

- Python 3.x
- pip

## Installation

1. Clone this repository:

```
$ git clone https://github.com/Tensornetics/compliment-bot.git
```

2. Install the dependencies:

```
$ pip install -r requirements.txt
```

## Running the Bot

To start the ComplimentBot, run the following command in your terminal:

```
$ python run.py
```

Then, navigate to `http://localhost:5000` in your web browser to see the ComplimentBot in action.

## Deployment

You can deploy the ComplimentBot to a cloud platform like Heroku or AWS to make it accessible to users worldwide.

## Built With

- Flask
- Python

## Author

Tensornetics LLC and OpenAI ChatGPT

```
compliment_bot/
    |
    ├── app/
    |   ├── __init__.py
    |   ├── compliment_generator.py
    |   ├── routes.py
    |   └── templates/
    |       └── index.html
    |
    ├── tests/
    |   └── test_compliment_generator.py
    |
    ├── config.py
    ├── requirements.txt
    └── run.py
```
