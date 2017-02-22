# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

# Flask
DEBUG = False
USE_RELOADER = False
SECRET_KEY = 'secret_key'

# SQLite
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'sqlite.db')

# MySQL
# host, port, database, user, password = '127.0.0.1', '3306', 'cihuahua', 'fauzi', 'O#ngis0479'
# SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (user, password, host, port, database)
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (user, password, host, port, database)

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
