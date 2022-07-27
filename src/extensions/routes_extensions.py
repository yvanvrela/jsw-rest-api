from flask import Flask
from apps.api.routes.auth_route import auth
from apps.api.routes.users_github import user_github


def register_routes(app: Flask) -> None:

    app.register_blueprint(auth)
    app.register_blueprint(user_github)
