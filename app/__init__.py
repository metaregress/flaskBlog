import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from flask.ext.babel import Babel, lazy_gettext
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.json import JSONEncoder
from speaklater import is_lazy_string
from .momentjs import momentjs
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

mail = Mail(app)

babel = Babel(app)

app.jinja_env.globals['momentjs'] = momentjs

class CustomJSONEncoder(JSONEncoder):
	"""This class adds support for lazy translation texts to flask's JSON Encoder. This is necessary when flashing translated texts"""
	def default(self, obj):
		if is_lazy_string(obj):
			try:
				return unicode(obj) #python 2
			except NameError:
				return str(obj)  #python 3
		return super(CustomJSONEncoder, self).default(obj)

app.json_encoder = CustomJSONEncoder


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
lm.login_message = lazy_gettext('Please log in to access this page.')
oid = OpenID(app, os.path.join(basedir, 'tmp'))

if not app.debug:
	#mail logging
	credentials = None
	if MAIL_USERNAME or MAIL_PASSWORD:
		credentials = (MAIL_USERNAME, MAIL_PASSWORD)
	mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'micro blog failure', credentials)
	mail_handler.setLevel(logging.ERROR)
	app.logger.addHandler(mail_handler)

	#file logging
	file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('microblog startup')
from app import views, models