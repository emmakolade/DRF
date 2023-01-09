import requests

endpoint = "http://localhost:8000/api/products/1/update"

data={
    "title": "Akolade",
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
# print(get_response.text)
# print(get_response.status_code)
