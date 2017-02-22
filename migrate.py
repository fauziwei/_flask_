# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import app
from app.model import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()

# python migrate.py db init
# python migrate.py db migrate
# python migrate.py db upgrade
