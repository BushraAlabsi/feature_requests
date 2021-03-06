from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from feature_req.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):

	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	# print(app.config['SECRET_KEY'])
	from .routes import featRequests
	app.register_blueprint(featRequests)

	return app


