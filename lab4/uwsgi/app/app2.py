import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def show_user_id():
    user_id = os.getuid()  # Get the user ID
    return f"Application running as user with ID: {user_id}"


if __name__ == "__main__":
    app.run()
