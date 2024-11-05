import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return f"Hello, it's zad2"


if __name__ == "__main__":
    app.run()
