import requests
import json
from authentication.Authentication import get_token

def process_payment():
	access_token= get_token()
	headers ={
	"Bearer %s" %(access_token["access_token"])
	}

	payload = {
   "CheckoutRequestID": "df88d1aa-9a19-448f-aa8b-40e4d7683f27"
   "MerchantCode": "95000"
   "VerificationCode": "535249"
	}

	url = ' https://api.sasapay.me/api/v1/payments/process-payment/'
	response = requests.post(url, headers, payload)
	return response
	data = json.loads(response.text)
	print(data)

process_payment()