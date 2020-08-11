import requests
import os
from pprint import pprint

url_base = "https://api.petfinder.com"

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

def get_token():    
    url = url_base + "/v2/oauth2/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        }
    r = requests.post(
        url=url,
        data=payload
    )
    data = r.json()
    return data['access_token']

TOKEN = get_token()

def decorator_request(func):
    def _decorator_request(**kwargs):
        kwargs = func(**kwargs)
        headers = {
            "Authorization": f"Bearer {TOKEN}",
        }
        r = requests.get(
            url=kwargs['url'], 
            headers=headers,
            params=kwargs['payload'],
        )
        data = r.json()
        return data
    return _decorator_request

@decorator_request
def get_animals(id=None, **kwargs):
    url = url_base + "/v2/animals"
    if id:
        url = url + f"/{id}"
    return {'url': url, 'payload': kwargs}

# params = {'type': 'dog', 'gender': 'male', 'age': 'baby', 'size': 'large'}
# pprint(get_animals(**params))
# pprint(get_animals(id=48605066))
# pprint(get_animals())

@decorator_request
def get_animal_types(type=None):
    url = url_base + "/v2/types"
    if type:
        url = url + f"/{type}"
    return {'url': url, 'payload': {}}

# pprint(get_animal_types())
# pprint(get_animal_types(type='rabbit'))

@decorator_request
def get_animal_breeds(type=None):
    url = url_base + "/v2/types/{type}/breeds"    
    return {'url': url, 'payload': {}}

# pprint(get_animal_breeds(type='cat'))

@decorator_request
def get_organizations(**kwargs):
    if 'href' in kwargs:
        url = url_base + kwargs.get('href')
    else:
        url = url_base + "/v2/organizations"
    return {'url': url, 'payload': kwargs}