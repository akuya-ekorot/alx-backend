#!/usr/bin/env python3
"""
Basic flask app
"""

from flask import Flask, render_template
from flask_babel import Babel, BabelConfiguration


class Config(BabelConfiguration):
    """config for the flask app"""

    LANGUAGES = ["en", "fr"]

    default_locale = "en"
    default_timezone = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def home() -> str:
    """Home route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
