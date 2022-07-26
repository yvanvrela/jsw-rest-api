from flask import Flask

from extensions import config_extension, routes_extensions


def create_app():
    app = Flask(__name__)

    config_extension.register_config(app)
    routes_extensions.register_routes(app)

    return app
