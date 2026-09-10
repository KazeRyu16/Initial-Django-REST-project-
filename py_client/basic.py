import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_responce = requests.get(endpoint, params={"abc":123}, json={"query": "Hello world"}) #HTTP request
print(get_responce.text)
print(get_responce.status_code)
print(get_responce.json())

