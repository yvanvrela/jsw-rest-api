from flask import Blueprint, jsonify, request
from ..function_jwt import write_token

auth = Blueprint('api_auth', __name__, url_prefix='/api/auth')


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'Yvan':
        return write_token(data=request.get_json())
    else:
        response = jsonify({'message': 'User not found'}), 404
        return response
