import requests
product_id = input("what product id do you want to delete? \n")
try:
    product_id=int(product_id)
except:
    print(f"{product_id} is not a valid id")

if product_id:
    endpoint = "http://localhost:8000/api/products/{product_id}/delete/"

    data = {
        "title": "Akolade",
    }

    get_response = requests.delete(endpoint, json=data)
    print(get_response.status_code, get_response.status_code==204)
# print(get_response.tex
# print(get_response.status_code)
