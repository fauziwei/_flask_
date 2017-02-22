# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

def create_app(configPy):

	# init Flask
	from flask import Flask
	app = Flask(__name__)
	app.config.from_object(configPy)

	# init database
	from app.model import db
	db.app = app
	db.init_app(app)

	# register main blueprint
	from app.main.view import mainBlueprint
	app.register_blueprint(mainBlueprint)

	# register role blueprint
	from app.role.view import roleBlueprint
	app.register_blueprint(roleBlueprint)

	# register user blueprint
	from app.user.view import userBlueprint
	app.register_blueprint(userBlueprint)

	return app
