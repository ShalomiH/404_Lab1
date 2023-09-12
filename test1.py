import requests

print(requests.__version__)

url = "https://raw.githubusercontent.com/ShalomiH/404_Lab1/main/test1.py"
print(requests.get("http://google.com/"))

res = requests.get(url)
print(res.text)