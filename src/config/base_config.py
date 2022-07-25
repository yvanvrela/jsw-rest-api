import os

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')