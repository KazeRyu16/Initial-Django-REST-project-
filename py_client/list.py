import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
Username = input("What is your username?\n")
password = getpass("What's your password?\n")

auth_response = requests.post(auth_endpoint,json={"username":Username ,"password":password})
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/product/"

    get_response = requests.get(endpoint,headers=headers)

    print(get_response.json())