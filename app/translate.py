try:
	import httplib #python 2
except ImportError:
	import http.client as httplib #python 3

try:
	from urllib import urlencode #python 2
except ImportError:
	from urllib.parse import urlencode #python 3
import json
from flask.ext.babel import gettext
from config import MS_TRANSLATOR_CLIENT_ID, MS_TRANSLATOR_CLIENT_SECRET

def microsoft_translate(text, sourceLang, destLang):
	if MS_TRANSLATOR_CLIENT_ID == "" or MS_TRANSLATOR_CLIENT_SECRET == "":
		return gettext("Error: translation service not configured")
	try:
		#get access token
		params = urlencode({
			'client_id': MS_TRANSLATOR_CLIENT_ID,
			'client_secret': MS_TRANSLATOR_CLIENT_SECRET,
			'scope': 'http://api.microsofttranslator.com',
			'grant_type': 'client_credentials'})
		conn = httplib.HTTPSConnection("datamarket.accesscontrol.windows.net")
		conn.request("POST", "/v2/OAuth2-13", params)
		response = json.loads(conn.getresponse().read())
		token = response[u'access_token']
	except:
		return gettext("Error: unable to get token.")

	try:
		#translate
		conn = httplib.HTTPConnection('api.microsofttranslator.com')
		params = {'appId': 'Bearer ' + token,
				  'from': sourceLang,
				  'to': destLang,
				  'text': text.encode("utf-8")}
		conn.request("GET", '/V2/Ajax.svc/Translate?' + urlencode(params))
		#response_json = "{\"response\":" + conn.getresponse().read().decode('utf-8') + "}"
		#print(response_json)
		#response = json.loads("{\"response\":" + conn.getresponse().read().decode('utf-8') + "}")
		response = conn.getresponse().read().decode('utf-8')
		return response
	except:
		return gettext("Error: unexpected error.")