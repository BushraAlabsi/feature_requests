import os

class TestConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

