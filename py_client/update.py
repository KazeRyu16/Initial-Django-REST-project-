import requests

headers = {'Authorization': 'Bearer fcdb5fe588d8f82bfa514adf2c696440979a73f3'}
endpoint = "http://127.0.0.1:8000/api/product/1/update"

data = {

"title":"Lego avengers",
"price":10,
"content":"Lego Avengers"

}

get_response = requests.put(endpoint,json = data,headers=headers)

print(get_response.json())