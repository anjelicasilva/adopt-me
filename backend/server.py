from flask import Flask, render_template, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
import time
import requests
import os


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

    
#############################################

if __name__ == '__main__':
    # connect_to_db(app)
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.run(debug=True,  host='0.0.0.0')
    # app.run(debug=True)
 
    #Use the DebugToolbar
    # DebugToolbarExtension(app)