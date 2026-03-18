

# 1. without dependencies
import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/posts"


try:
    response = urllib.request.urlopen(url)
    data = response.read()
    json_data = json.loads(data.decode("utf-8"))
    print(json_data)
    response.close()
except Exception as e:
    print(e)
finally:
    response.close()

