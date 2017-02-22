# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from app.model import db, CRUD

class Role(db.Model, CRUD):
	__tablename__ = 'role'
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(250), nullable=True, unique=True)
	description = db.Column(db.String(250))
	user = db.relationship('User', backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role %s>' % self.name
