import requests
import os
from pprint import pprint

url_base = "https://api.petfinder.com"

def get_token():
    url = url_base + '/v2/oauth2/token'
    data = {'grant_type': 'client_credentials',
            'client_id': os.environ['CLIENT_ID'],
            'client_secret': os.environ['CLIENT_SECRET']}
    response = requests.post(url, data=data)
    res = response.json()
    token = res['token_type'] + ' ' + res['access_token']
    return token

def get_response_data(url, token, payload=None):
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    return data

def get_animals(id=None, **kwargs):
    token = get_token()
    url = url_base + "/v2/animals"
    if id:
        url = url + f"/{id}"
    return get_response_data(url, token, payload=kwargs)

def get_organization(href):
    token = get_token()
    url = url_base + href
    return get_response_data(url, token)

pprint(get_organization("/v2/organizations/ia36"))