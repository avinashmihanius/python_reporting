import requests
from requests.auth import HTTPDigestAuth
import json
import pprint
import sys
import xlsxwriter


def getJson():

    # url = 'https://jsonplaceholder.typicode.com/todos/1'
    url = 'https://reqres.in/api/users?page=2'

    myResponse = requests.get(url, verify=True)
    myResponse_json = myResponse.json()
    # data = json.dumps(myResponse_json, indent=2, sort_keys=True)
    
    with open('response.json', 'w') as f:
        json.dump(myResponse_json, f)

getJson()