import requests
import json
from requests.auth import HTTPBasicAuth

def get_token():
	params= {"grant_type": "client_credentials"}
	CLIENT_ID = "fZfvfWxAoF31xhtHFP4uWRgFxRwbm8oMdTejGi8w"
	CLIENT_SECRET = "rrZ0uT7oO79SHUouojfJxryjnBaph9IZDfqW17F4Adxn8LGPywRm1ScrrzkzwuWpx37p2yHrfJLSr1LEIusWcGJjGeev5jRPObvys6NR5JQC5cz1HYJqpWQa9WCHP9VZ"
	url = 'https://api.sasapay.me/api/v1/auth/token/'
	response = requests.get(url, Authorization=HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET), params=params)
	data = json.loads(response.text)
	return response
	