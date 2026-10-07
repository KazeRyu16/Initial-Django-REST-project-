import requests

product_id =input("What is the product id you want to use?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid')

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/product/{product_id}/delete"

    get_responce = requests.delete(endpoint)
    print(get_responce.status_code)