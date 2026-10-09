import requests

endpoint = "http://127.0.0.1:8000/api/product/9/update"

data = {

"title":"heyAmir",
"price":10,
"content":"Testfield"

}

get_response = requests.put(endpoint,json = data,)

print(get_response.json())