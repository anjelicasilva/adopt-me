import requests
import os

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

def get_animal_types():
    url = "https://api.petfinder.com/v2/types"
    # headers = {
    #     "client_id": API_KEY,
    #     "client_secret": SECRET,
    # }
    r = requests.get(
        url, 
        # headers=headers,
    )
    data = r.json()
    print(r)
    print(data)

