import requests

BASE_URL = 'http://127.0.0.1:8003'

MOCK_USER_DATA = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}

MOCK_USER_CREATE = {
    "id": 25,
    "email": "tests.test_2@tests.tests",
    "first_name": "Test",
    "last_name": "Test_2",
    "avatar": "https://test"
}


def test_get_single_user():
    response = requests.get(f'{BASE_URL}/api/users/{MOCK_USER_DATA["data"]["id"]}')
    assert response.status_code == 200
    result = response.json()

    assert result["data"]["id"] == MOCK_USER_DATA["data"]["id"]


def test_get_singler_user_not_found():
    response = requests.get(f'{BASE_URL}/api/users/545')

    assert response.status_code == 404


def test_create_user():
    response = requests.post(f'{BASE_URL}/api/users', json=MOCK_USER_CREATE)
    assert response.status_code == 200

    result = response.json()
    assert result["first_name"] == MOCK_USER_CREATE["first_name"] and result["id"] == MOCK_USER_CREATE["id"]


def test_delete_user():
    response = requests.delete(f'{BASE_URL}/api/users/{MOCK_USER_DATA["data"]["id"]}')
    assert response.status_code == 204


