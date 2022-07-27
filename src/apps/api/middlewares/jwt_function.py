from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify


def expire_date(hours: int) -> int:
    now_date = datetime.now()
    expire_date = now_date + timedelta(hours=hours)

    return expire_date


def write_token(data: dict, hours_expire=24):
    token = encode(
        payload={**data, 'exp': expire_date(hours=hours_expire)},
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
        response = jsonify({'message': 'Invalid Token'}), 401
        return response

    except exceptions.ExpiredSignatureError:
        response = jsonify({'message': 'Token Expired'}), 401
        return response
