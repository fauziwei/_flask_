# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from flask import Blueprint, request
from flask_restful import Api, reqparse
from app.view import Resource
from app.model import db
from app.role.model import Role
from sqlalchemy.exc import SQLAlchemyError
from log import logger

roleBlueprint = Blueprint('role', __name__)
api = Api(roleBlueprint)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('name', type=str)
parser.add_argument('description', type=str)

class Roles(Resource):

	# Display roles
	def get(self):
		args = request.args
		logger.debug('Role is accessed.')
		return { 'Status': True }

	# Create role
	def post(self):
		args = parser.parse_args()
		pass

	# Update role
	def put(self):
		args = parser.parse_args()
		pass

	# Delete role
	def delete(self):
		args = parser.parse_args()
		pass


api.add_resource(Roles, '/role/')
