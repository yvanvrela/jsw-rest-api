from flask import Blueprint, jsonify, request
from itsdangerous import SignatureExpired, BadSignature
from apps.api.middlewares.confirm_email_function import send_email_token, SERIALIZE
from ..middlewares.jwt_function import validate_token, write_token

auth = Blueprint('api_auth', __name__, url_prefix='/api/auth')


@auth.route('/login', methods=['POST'])
def login():
    data_complete = request.get_json()
    data = {'id': data_complete['id'], 'username': data_complete['username']}
    if data['username'] == 'Yvan':
        return write_token(data=data)
    else:
        response = jsonify({'message': 'User not found'}), 404
        return response


@auth.route('/verify/token')
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    user_data = request.get_json()

    # registro en la base de datos
    # id, email, password, rol, email_validate

    email = user_data['email']
    send_email_token(email)

    response = jsonify({'message': 'Verify your email'}), 200

    return response


@auth.route('/confirm_email/<token>', methods=['GET'])
def confirm_email(token):
    try:
        SERIALIZE.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        return jsonify({'message': 'Token expired'})
    except BadSignature:
        return jsonify({'message': 'Token not match!'})
    return jsonify({'message': 'Token works!'}), 200
