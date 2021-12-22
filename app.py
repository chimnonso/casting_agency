import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_cors import CORS

from models import *


def create_app(test_config=None):
	app = Flask(__name__)
	setup_db(app)

	# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
	# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:foobar@localhost:5432/casting_agency"
	# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# db = SQLAlchemy(app)
	# Migrate(app, db)


	@app.route('/')
	def home():
		return jsonify({
			"success": True,
			"message": "Hello World"
		})
		
	return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80, debug=True)