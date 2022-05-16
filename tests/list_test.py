"""System module."""
import requests
BASE_URL = "http://127.0.0.1:5002/"
def test_fetch_user() :
    """Doc String"""
    path = "list"
    response = requests.get(url=BASE_URL+path)
    assert response.status_code == 200
    