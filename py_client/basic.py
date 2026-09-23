import requests
import json

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_responce = requests.get(endpoint, params={"abc":123}, json={"query": "Hello world"}) #HTTP request
# print(get_responce.text) prints raw text response (which means the source code of the endpoint)
print(get_responce.status_code) # prints the status code (200 means working successfully and so on )
print(get_responce.json()) # prints the json response ( json refers to javascript object notation)