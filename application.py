from flask import Flask

import requests


def breaking_quote():
    url = "https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes"
    call = requests.get(url).json()[0]
    response = f"{call['author']} says : {call['quote']}"
    return response


application = Flask(__name__)


@application.route("/")
def index():
    return "<h1>Hello guys!!</h1>"


@application.route("/quote")
def quote():
  random_quote = breaking_quote()
  return {"quote": random_quote}


if __name__ == "__main__":
    application.run(debug=True)
