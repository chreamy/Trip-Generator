import requests
import base64
import json
import pprint
import os

def upload(path):
    params = {
    'expiration': '600',
    'key': 'ae2813aa3142a0c191f6bc32f0fbe44a',
    }

    files = {
    'image': (None,base64.b64encode(open(path, "rb").read()))
    }
    response = requests.post('https://api.imgbb.com/1/upload', params=params, files=files)
    print(json.loads(response.text)['data']['url'])
    os.remove(path)
    return json.loads(response.text)['data']['url']