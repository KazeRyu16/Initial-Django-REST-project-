import requests

headers = {'Authorization': 'Bearer f338d86d757000aca4623f57de1f4531f45c21c6'}
endpoint = "http://127.0.0.1:8000/api/product/"

data = {

"title":"This is a create view",
"price":120
}

get_response = requests.post(endpoint,json = data,headers=headers)

print(get_response.json())

