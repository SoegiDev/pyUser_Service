import sys
sys.path.append('./')
import json
import pytest
import app

@pytest.fixture
def client(request):
    test_client = app.app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def test_login(client):
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
    url = '/login'
    response = client.post(url,data=json.dumps(data),headers = headers)
    assert response.status_code == 500