import logging
import sys

from flask import Flask, url_for, render_template, request

from main.config import Config

app = Flask(__name__)

def make_app(config = None, testing = None):
    if not config:
        if not testing:
            testing = False
        config = Config(testing=testing)

    # Create a Flask app object.

    app.config.from_object(config)

    import main.views as views
    app.register_blueprint(views.base.blueprint)

    return app

if __name__ == "__main__":
    config = Config()
    app = make_app(config)
    app.run(port=config.port)
