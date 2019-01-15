import os
import json

#used for the deployed version
# with open('/etc/config.json') as config_file:
# 	config = json.load(config_file)

class Config:

	#used for the deployed version
	# SQLALCHEMY_DATABASE_URI=config.get('SQLALCHEMY_DATABASE_URI')
	# SECRET_KEY=config.get('SECRET_KEY')

	#to run on locally
	SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
	SECRET_KEY=os.environ.get('SECRET_KEY')
	SQLALCHEMY_TRACK_MODIFICATIONS= False
