import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass()

auth_response = requests.post(auth_endpoint,json={"username":"ryu" ,"password":password})
print(auth_response.json())



endpoint = "http://127.0.0.1:8000/api/product/"

get_response = requests.get(endpoint)

print(get_response.json())