# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from app import create_app
app = create_app('config')

if __name__ == '__main__':
	host, port = '0.0.0.0', 5555
	app.run(host=host, port=port)
