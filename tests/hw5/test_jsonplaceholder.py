import requests
import json
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/"


def test_validate_statuscode():
    response = requests.get(BASE_URL + "todos/1")
    assert response.status_code == 200, "Wrong status code" + str(response.status_code)


def test_invalidate_statuscode():
    invalid_response = requests.get(BASE_URL + "/123")
    assert invalid_response.status_code == 404, "Expected 404 status code" + str(invalid_response.status_code)


def test_validate_comments():
    response = requests.get(BASE_URL + "/comments")
    data = json.loads(response.content)
    size_of_data = len(data)

    assert size_of_data == 500


@pytest.mark.parametrize(("user_id", "email"),
                         [("1", "Sincere@april.biz"),
                          ("2", "Shanna@melissa.tv"),
                          ("3", "Nathan@yesenia.net")])
def test_validate_users(user_id, email):
    response = requests.get(BASE_URL + "/users/" + user_id)
    data = json.loads(response.content)

    assert data["email"] == email


@pytest.mark.parametrize(("post_id", "title"),
                         [("1", "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
                          ("2", "qui est esse")])
def test_validate_users(post_id, title):
    response = requests.get(BASE_URL + "/posts/" + post_id)
    data = json.loads(response.content)

    assert data["title"] == title
