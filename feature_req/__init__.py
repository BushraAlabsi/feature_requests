from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  feature_req.config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

from feature_req import routes