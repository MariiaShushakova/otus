import requests

proxy = {"http": "localhost:8080", "https:": "localhost:8080"}

requests.get("https://www.google.com/", proxies=proxy, verify=False)