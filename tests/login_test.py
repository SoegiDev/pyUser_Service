"""System module."""
import json
import requests
BASE_URL = "http://127.0.0.1:5002/"
def login() :
    """Doc String"""
    path = "login"
    mimetype = 'application/json'
    username = 'soegidev'
    password= 'fajarsoegi'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(BASE_URL+path,data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    