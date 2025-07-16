import requests
from pprint import pprint

API_URL="http://localhost:8000/"

response=requests.get(API_URL)
print(response.json())
