import requests

endpoint = "http://127.0.0.1:8000/api/product/"

data = {

"title":"This is a create view",
"price":120
}

get_response = requests.post(endpoint,json = data)

print(get_response.json())