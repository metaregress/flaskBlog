# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') +
                               '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True
# slow databse query threshold
DATABASE_QUERY_TIMEOUT = 0.5

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

WTF_CSRF_ENABLED=True
SECRET_KEY='sooper-sekret-key'

POSTS_PER_PAGE=5

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

#microsoft translate creds
MS_TRANSLATOR_CLIENT_ID = 'flaskTestTranslation'
MS_TRANSLATOR_CLIENT_SECRET = 'JvzFsK5ZY/NVfdmw7BibhJou2uMxmDPzPS9ePUIWbVo='

#mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

#Administrator List
ADMINS = ['metaregress@gmail.com']

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]