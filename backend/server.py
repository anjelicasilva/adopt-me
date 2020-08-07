from flask import Flask, render_template, jsonify, request, Response
# from flask_debugtoolbar import DebugToolbarExtension
import time
import requests
import os
from petfinderapi import get_animals, get_organization

app = Flask(__name__)

# Key required to run Flask sessions and for the debug toolbar
app.secret_key = 'adoptme'

# Rather than failing silently, undefined variables in Jinja2 raise an error.
# app.jinja_env.undefined = StrictUndefined


def get_token():
    url = 'https://api.petfinder.com/v2/oauth2/token'
    data = {'grant_type': 'client_credentials',
            'client_id': os.environ['CLIENT_ID'],
            'client_secret': os.environ['CLIENT_SECRET']}
    response = requests.post(url, data=data)
    res = response.json()
    token = res['token_type'] + ' ' + res['access_token']
    return token


def get_response_data(url, token, payload):
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    return data


@app.route('/breeds.json')
def get_all_breeds():
    """ INPUT DOCSTRING HERE """

    ### EXAMPLE DOG BREED SELECTION ###
    breed_type = 'dog'
    token = get_token()
    url = 'https://api.petfinder.com/v2/types/'+ breed_type +'/breeds'
    payload = {
        'type': breed_type
    }
    data = get_response_data(url, token, payload)
    breeds = {}
    breeds['breeds'] = []
    for breed in data['breeds']:
        breeds['breeds'].append(breed['name'])

    return jsonify(breeds)


@app.route('/locations.json')
def get_all_locations():
    """ INPUT DOCSTRING HERE """

    #### EXAMPLE BRISBANE ZIP CODE ####
    location_type = '94005'
    token = get_token()
    url = 'https://api.petfinder.com/v2/organizations/'
    headers = {'Authorization': token}
    payload = {
        'location': location_type
    }
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    organizations = {}
    organizations['name'] = []
    for organization in data['organizations']:
        organizations['name'].append(organization['name'])

    return jsonify(organizations)


@app.route('/search')
def search_results():
    payload = request.args.to_dict()
    data = get_animals(**payload)
    results = []
    for data_animal in data['animals']:
        animal = {}

        # data on search results
        animal['photos'] = data_animal['photos']
        animal['name'] = data_animal['name']
        animal['breeds'] = data_animal['breeds']
        animal['gender'] = data_animal['gender']
        animal['age'] = data_animal['age']

        # more data for individual pet page
        animal['description'] = data_animal['description']
        animal['status'] = data_animal['status']
        animal['declawed'] = data_animal['attributes']['declawed']
        animal['house_trained'] = data_animal['attributes']['house_trained']
        animal['shots_current'] = data_animal['attributes']['shots_current']
        animal['spayed_neutered'] = data_animal['attributes']['spayed_neutered']
        animal['special_needs'] = data_animal['attributes']['special_needs']
        animal['tags'] = data_animal['tags']
        animal['videos'] = data_animal['videos']
        animal['size'] = data_animal['size']
        animal['good_with_children'] = data_animal['environment']['children']
        animal['good_with_dogs'] = data_animal['environment']['dogs']
        animal['good_with_cats'] = data_animal['environment']['cats']
        animal['contact_address'] = data_animal['contact']['address']
        animal['contact_email'] = data_animal['contact']['email']
        animal['contact_phone'] = data_animal['contact']['phone']
        organization = get_organization(href=data_animal['_links']['organization']['href'])
        animal['organization_name'] = organization['organization']['name']

        results.append(animal)
    return jsonify(results)

#############################################

if __name__ == '__main__':
    # connect_to_db(app)
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.run(debug=True,  host='0.0.0.0')
    # app.run(debug=True)
 
    #Use the DebugToolbar
    # DebugToolbarExtension(app)