"""System module."""
import requests
BASE_URL = "http://127.0.0.1:5002/"
def singleuser() :
    """Doc String"""
    path = "single?username=soegidev"
    mimetype = 'application/json'
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = requests.get(BASE_URL+path,headers = headers)
    assert response.status_code == 200
    