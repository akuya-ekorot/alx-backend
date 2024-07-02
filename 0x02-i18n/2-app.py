#!/usr/bin/env python3
"""
Basic flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel, BabelConfiguration


class Config(BabelConfiguration):
    """config for the flask app"""

    LANGUAGES = ["en", "fr"]

    default_locale = "en"
    default_timezone = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home() -> str:
    """Home route"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
