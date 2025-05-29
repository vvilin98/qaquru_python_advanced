import requests


BASE_URL = 'https://reqres.in'
headers = {'x-api-key': 'reqres-free-v1'}

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
    "name": "Test",
    "job": "QA",
    "id": "25"
}

MOCK_USER_UPDATE = {
    "name": "Test_2",
    "job": "QA_2"
}


def test_get_singler_user():
    response = requests.get(f'{BASE_URL}/api/users/{MOCK_USER_DATA["data"]["id"]}', headers=headers)
    assert response.status_code == 200

    result = response.json()

    assert result["data"]["id"] == MOCK_USER_DATA["data"]["id"]


def test_get_singler_user_not_found():
    response = requests.get(f'{BASE_URL}/api/users/545', headers=headers)
    assert response.status_code == 404 and not response.json(), f'json не пуст'


def test_create_user():
    response = requests.post(f'{BASE_URL}/api/users', headers=headers, data=MOCK_USER_CREATE)
    assert response.status_code == 201

    result = response.json()
    assert result["name"] == MOCK_USER_CREATE["name"] and result["id"] == MOCK_USER_CREATE["id"]


def test_update_user():
    r_post = requests.post(f'{BASE_URL}/api/users', headers=headers, data=MOCK_USER_CREATE)
    assert r_post.status_code == 201 and r_post.json()["id"] == MOCK_USER_CREATE["id"]

    r_put = requests.put(f'{BASE_URL}/api/users/{r_post.json()["id"]}', headers=headers, data=MOCK_USER_UPDATE)

    result = r_put.json()
    assert result["name"] == MOCK_USER_UPDATE["name"] and result["job"] == MOCK_USER_UPDATE["job"]


def test_delete_user():
    response = requests.delete(f'{BASE_URL}/api/users/{MOCK_USER_DATA["data"]["id"]}', headers=headers)
    assert response.status_code == 204
