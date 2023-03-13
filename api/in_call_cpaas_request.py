import requests

url = "http://localhost:5005/api/incall"
payload={}
response = requests.request("POST", url,data=payload)
print(response.text)
