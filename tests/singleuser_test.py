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

def test_single_user(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = '/single?username=soegidev'
    response = client.get(url,headers = headers)
    assert response.status_code == 500