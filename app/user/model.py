# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from app.model import db, CRUD

class User(db.Model, CRUD):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)

	email = db.Column(db.String(250), nullable=False, unique=True)
	password = db.Column(db.String(250), nullable=False)
	firstname = db.Column(db.String(250))
	lastname = db.Column(db.String(250))
	role = db.Column(db.String(250), db.ForeignKey('role.name'))
	active = db.Column(db.Integer, nullable=False)
	create = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

	def is_active(self):
		return True

	def get_id(self):
		return self.email

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		return

	def __init__(self, email, password, firstname, lastname, role, active):
		self.email = email
		self.password = password
		self.firstname = firstname
		self.lastname = lastname
		self.role = role
		self.active = active

	def __repr__(self):
		return '<User %s>' % self.email
