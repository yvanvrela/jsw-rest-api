import os
from .base_config import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
