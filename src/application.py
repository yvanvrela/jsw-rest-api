from flask import Flask

from extensions import config_extension


def create_app():
    app = Flask(__name__)

    config_extension.register_config(app)

    return app
