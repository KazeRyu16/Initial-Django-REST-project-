import requests
import json

endpoint = "http://127.0.0.1:8000/api/product/10/"

get_responce = requests.get(endpoint) #HTTP request
# print(get_responce.headers)

print(get_responce.json())  