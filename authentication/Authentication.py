import requests
import json
from requests.auth import HTTPBasicAuth

def get_token():
	params= {"grant_type": "client_credentials"}
	client_id = settings.CLIENT_ID
	client_secret = settings.CLIENT_SECRET
	url = 'https://api.sasapay.me/api/v1/auth/token/'
	response = requests.get(url, Authorization=HTTPBasicAuth(client_id,client_secret), params=params)
	data = json.loads(response.text)
	return response
	