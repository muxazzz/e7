import requests

url = "http://localhost:5000/message"

payload = {'text':'dsdsds'}
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))