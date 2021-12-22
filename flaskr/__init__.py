import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import *
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
	app = Flask(__name__)
	setup_db(app)
	CORS(app)

	# CORS Headers
	@app.after_request
	def after_request(response):
		response.headers.add(
			'Access-Control-Allow-Headers',
			'Content-Type, Authorization,true'
		)
		response.headers.add(
			'Access-Control-Allow-Methods',
            'GET, POST, PATCH, DELETE, OPTIONS'
		)
        return response


	@app.route('/')
	def home():
		return jsonify({
			"success": True,
			"message": "Hello World"
		})

	# @app.route('/movies', methods='GET')
	# @requires_auth('get:movies')
	# def get_movies(payload):
	
		
	return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80, debug=True)