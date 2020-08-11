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

def get_response_data(url, token, **payload):
    headers = {'Authorization': token}
    # if not payload:
    #     payload = {}
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    # Todo: pagination, handle rate limit of 1000/day and 50/second
    # if 'pagination' in data and data['pagination'].get('current_page')!=data['pagination'].get('total_pages'):
    #     payload['page'] = data.get('current_page',0) + 1
    #     token = token()
    #     data = get_response_data(url, token=token, payload=params)
    #     data = response.json()
    return data

def get_animals(id=None, **kwargs):
    token = get_token()
    print('kwargs:', kwargs)
    url = url_base + "/v2/animals"
    if id:
        url = url + f"/{id}"
    return get_response_data(url, token, payload=kwargs)

def get_organizations(**kwargs):
    token = get_token()
    if 'href' in kwargs:
        url = url_base + kwargs.get('href')
    else:
        url = url_base + "/v2/organizations"
    return get_response_data(url, token)