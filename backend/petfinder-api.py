import requests
import os
from pprint import pprint

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")

def get_token():    
    url = "https://api.petfinder.com/v2/oauth2/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": SECRET,
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
    url = "https://api.petfinder.com/v2/animals"
    if id:
        url = url + f"/{id}"
    return {'url': url, 'payload': kwargs}

# pprint(get_animals(type='cat', location="san francisco, ca", limit="2"))
# pprint(get_animals(id=48605066))
# pprint(get_animals())

@decorator_request
def get_animal_types(type=None):
    url = "https://api.petfinder.com/v2/types"
    if type:
        url = url + f"/{type}"
    return {'url': url, 'payload': {}}

# pprint(get_animal_types())
# pprint(get_animal_types(type='rabbit'))

@decorator_request
def get_animal_breeds(type=None):
    url = f"https://api.petfinder.com/v2/types/{type}/breeds"    
    return {'url': url, 'payload': {}}

# pprint(get_animal_breeds(type='cat'))

@decorator_request
def get_organizations(**kwargs):
    url = "https://api.petfinder.com/v2/organizations"
    return {'url': url, 'payload': kwargs}

# pprint(get_organizations(location="san francisco, ca", country="US", limit=2))
# pprint(get_organizations())