import requests
import json

endpoint = "http://127.0.0.1:8000/api/"

get_responce = requests.get(endpoint, params={"abc":123}, json={"query": "Hello world"}) #HTTP request
# print(get_responce.headers)

print(get_responce.status_code) # prints the status code (200 means working successfully and so on )
print(get_responce.json())  