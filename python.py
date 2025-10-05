import requests

response = requests.get("https://habr.com/ru/articles/")

print(response.headers)