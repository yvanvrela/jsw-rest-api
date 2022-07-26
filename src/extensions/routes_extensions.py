from flask import Flask
from apps.api.routes.auth_route import auth


def register_routes(app: Flask) -> None:

    app.register_blueprint(auth)
