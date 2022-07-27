from flask import Blueprint, request
from ..middlewares.jwt_function import validate_token
from requests import get


user_github = Blueprint('users_github', __name__, url_prefix='/api/github')


@user_github.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(' ')[1]
    validate_token(token, output=False)


@user_github.route('/users', methods=['POST'])
def github():
    data = request.get_json()
    country = data['country']
    return get(f'https://api.github.com/search/users?q=location:"{country}"&page=1').json()
