from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '26491f801b9edd98a9035e08f95a93d8'

from feature_req import routes