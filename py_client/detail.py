import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
Username = input("enter username\n")
Password = getpass("Enter the password?\n")

auth_responce = requests.post(auth_endpoint,json={"username":Username,"password":Password})
print(auth_responce.json())

if auth_responce.status_code == 200:
    token = auth_responce.json()['token']
    headers = {
        "Authorization" : f"Token {token}"
    }

    endpoint = "http://127.0.0.1:8000/api/product/1/"

    get_responce = requests.get(endpoint,headers=headers) #HTTP request
    # print(get_responce.headers)

    print(get_responce.json())  