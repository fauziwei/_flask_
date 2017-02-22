# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

import os.path
import time
import logging
from   logging.handlers import TimedRotatingFileHandler

basedir = os.path.abspath(os.path.dirname(__file__))
logpath = os.path.join(basedir, 'log', 'debug')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] %(message)s', '%Y-%m-%d %H:%M:%S')

filehandler = TimedRotatingFileHandler(logpath, 'D', 1, 0)
filehandler.setFormatter(formatter)

filehandler.suffix = '%Y-%m-%d_%H:%M:%S'
logger.addHandler(filehandler)
