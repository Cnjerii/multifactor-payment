import requests
import json
from requests.auth import HTTPBasicAuth
from authentication.Authentication import get_token

def request_payment():
	access_token= get_token()
	headers ={
	"Bearer %s" %(access_token["access_token"])
	}

	payload = {
   		"MerchantCode": "95000",
   		"PhoneNumber": "254745742007",
   		"TransactionDesc": "Request by Mobile Number",
   		"AccountReference": "254745742007",
   		"Currency": "KES",
   		"Amount": 10,
   		"CallBackURL": "https://posthere.io/d911-4959-8ef9"
	}

	url = 'https://api.sasapay.me/api/v1/payments/request-payment/'
	response = requests.post(url, headers, payload)
	return response
	data = json.loads(response.text)
	print(data)

request_payment()
