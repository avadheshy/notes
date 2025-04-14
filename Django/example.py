a=10
b=1
import json
url="https://hrmsapi.superworks.com/efefe"
# url="https://hrmsapi.superworks.com/"
import requests
try:
    res=requests.get(url=url)
    print(res.status_code)
    print(res.text)
    res=json.loads(res.text)
except Exception as e:
    print(e)
else:
    print("no exception")
finally:
    print("final code")