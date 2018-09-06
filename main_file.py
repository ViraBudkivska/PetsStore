import requests
import sys
resp = requests.get('http://petstore.swagger.io/#/')
try:
    print(resp.status_code)
    print(resp.headers)
    print(resp.text)
except Exception:
    print("oops we have a problem!")
    print(sys.exc_info())
    exit()

print("Everything okekkky")
