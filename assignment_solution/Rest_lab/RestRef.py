

# Reference To call a GET API
'''
import requests


response = requests.get(<<GET API URL>>)

print(json.dumps(response.json(), indent=4))

'''


import json
import requests
from types import SimpleNamespace

response = requests.get("http://localhost:8080/employees")
print(response.json())

def convertJsonStringToPythonObj(responseJsonString):
    responseObject = json.loads(
        responseJsonString, object_hook=lambda d: SimpleNamespace(**d))
    return responseObject

# to print the rest response in readable json format.


def printRestResponse(response):
    print(json.dumps(response.json(), indent=4))