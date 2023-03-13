import requests

press_digits="3"
url = "http://localhost:5005/api/process_digits"
payload={}
data = {"digits":press_digits,"readstatus":press_digits}
response = requests.request("POST", url,data=payload,json=data)
print(response.text)
