# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class CRUD:

	def add(self, obj):
		db.session.add(obj)
		return db.session.commit()

	def update(self):
		return db.session.commit()

	def delete(self, obj):
		db.session.delete(obj)
		return db.session.commit()
