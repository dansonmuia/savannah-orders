# Functions to perform common http requests

import json

from app.auth.tokens import generate_access_token


def get_headers(user=None):
    headers = {'content-type': 'Application/json'}
    if user:
        headers['Authorization'] = generate_access_token(user)

    return headers


def post(client, url, data, login_with=None):
    response = client.post(url, data=json.dumps(data), headers=get_headers(login_with))
    return response, response.get_json()


def get(client, url, login_with=None):
    response = client.get(url, headers=get_headers(login_with))
    return response, response.get_json()


def put(client, url, data, login_with=None):
    response = client.put(url, data=json.dumps(data), headers=get_headers(login_with))
    return response, response.get_json()
