

# 1. without dependencies
import requests
import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/posts"


try:
    response = urllib.request.urlopen(url)
    data = response.read()
    json_data = json.loads(data.decode("utf-8"))
    print(json_data)
except Exception as e:
    print(e)
finally:
    response.close()


# 2. with dependency - GET
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.json())

# 2. with dependency - POST
input = {
    "title": "foo",
    "body": "bar",
    "userId": 5
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", input)
print(response.json())
print(response.status_code)
