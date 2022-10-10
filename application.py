import requests
from flask import Flask

application = Flask(__name__)


def breaking_quote():
    url = "https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes"
    call = requests.get(url).json()[0]
    response = f"{call['author']} says : {call['quote']}"
    return response


@application.route("/")
def index():
    return "<h1>Hello world </h1>"


@application.route("/quote")
def quote():
  random_quote = breaking_quote()
  return {"quote": random_quote}


if __name__ == "__main__":
    application.run(debug=True)
