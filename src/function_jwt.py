from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify


def expire_date(days: int) -> int:
    now_date = datetime.now()
    expire_date = now_date - timedelta(days)

    return expire_date


def write_token(data: dict):
    token = encode(
        payload={**data, 'exp': expire_date(1)},
        key=getenv('SECRET_KEY'),
        algorithm='HS256'
    )

    return token.encode('UTF-8')


def validate_token(token: str, output=False):
    try:
        if output:
            return decode(token, key=getenv('SECRET_KEY'), algorithms=['HS256'])
        decode(token, key=getenv('SECRET_KEY'), algorithms=['HS256'])

    except exceptions.DecodeError:
        response = jsonify({'message': 'Invalid Token'})
        response.status_code = 401
        return response

    except exceptions.ExpiredSignatureError:
        response = jsonify({'message': 'Token Expired'})
        response.status_code = 401
        return response
