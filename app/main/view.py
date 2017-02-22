# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from flask import Blueprint, request
from flask_restful import Api, reqparse
from app.view import Resource
from app.model import db
# from app.main.model import Main
from sqlalchemy.exc import SQLAlchemyError
from log import logger

mainBlueprint = Blueprint('main', __name__)
api = Api(mainBlueprint)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)

class Index(Resource):

	# Get something
	# curl -i http://localhost:5555/
	def get(self):
		logger.debug('main is accessed.')
		return { 'status': True }

	# Create something
	def post(self):
		args = parser.parse_args()

	# Update something
	def put(self):
		args = parser.parse_args()

	# Delete something
	def delete(self):
		args = parser.parse_args()


api.add_resource(Index, '/', '/main/')
