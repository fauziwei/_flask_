# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from hashlib import sha1
from datetime import datetime
from flask import Blueprint, request
from flask_restful import Api, reqparse
from app.view import Resource
from app.model import db
from app.user.model import User
from sqlalchemy.exc import SQLAlchemyError
from log import logger

userBlueprint = Blueprint('user', __name__)
api = Api(userBlueprint)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)
parser.add_argument('firstname', type=str)
parser.add_argument('lastname', type=str)
parser.add_argument('role', type=str)
parser.add_argument('active', type=str)

class Users(Resource):

	# Get list of user/ single user/ list of user based on its role
	# curl -i http://localhost:5555/user/
	# curl -i http://localhost:5555/user/?id=1
	# curl -i http://localhost:5555/user/?role=1
	def get(self):
		logger.debug('User is accessed.')
		return { 'status': True }

	# Create user
	# curl -i http://localhost:5555/user/ -H "Content-Type: application/json" -X POST -d '{"email":"xxx@soovii.com", "password":"xxx", "firstname":"triple", "lastname":"x", "role":"2"}'
	def post(self):
		args = parser.parse_args()

	# Update user
	# curl -i http://localhost:5555/user/ -H "Content-Type: application/json" -X PUT -d '{"id": "2", "email":"xxx@soovii.com", "password":"xxx", "firstname":"triple", "lastname":"xxx", "role_id":"2"}'
	def put(self):
		args = parser.parse_args()

	# Delete user
	# curl -i http://localhost:5555/user/ -H "Content-Type: application/json" -X DELETE -d '{"id":"2"}'
	def delete(self):
		args = parser.parse_args()


api.add_resource(Users, '/user/')
