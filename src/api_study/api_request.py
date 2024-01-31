import requests

headers = {
    "User-Agent": "python"
}
#GET request
response = requests.get("https://httpbin.org/get", headers=headers) # , params={'a':'b', 'c':10})
if response.ok:
    print("OK")

print(response.text)

#POST request
response = requests.post("https://httpbin.org/post",
                         headers=headers,
                         json={'username': 'admin'})

print(response.text)

