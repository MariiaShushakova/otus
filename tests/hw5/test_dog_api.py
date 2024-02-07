import requests
import json
import pytest

from src.test_data.file_path2 import JSON_FILE_LIST_DOGS

BASE_URL = "https://dog.ceo/api/"


def test_validate_statuscode():
    response = requests.get(BASE_URL + "breeds/list/all")
    assert response.status_code == 200, "Wrong status code" + str(response.status_code)


def test_invalidate_statuscode():
    invalid_response = requests.get(BASE_URL + "breeds/list/all123")
    assert invalid_response.status_code == 404, "Expected 404 status code" + str(invalid_response.status_code)


@pytest.mark.parametrize(("breed", "img"),
                         [("hound/afghan", "https://images.dog.ceo/breeds/hound-afghan/"),
                          ("australian/shepherd", "https://images.dog.ceo/breeds/australian-shepherd/"),
                          ("bulldog/boston", "https://images.dog.ceo/breeds/bulldog-boston/")],
                         ids=["afghan", "shepherd", "boston"])
def test_verify_img(breed, img):
    response = requests.get(BASE_URL + "breed/" + breed + "/images/random")
    data = json.loads(response.content)
    str_img = str(data["message"])

    assert str_img.startswith(img)


@pytest.mark.parametrize("num_of_img",
                         [1, 3, 50],
                         ids=["1-img", "3-img-s", "50-img-s"])
def test_verify_number_of_imgs(num_of_img):
    response = requests.get(BASE_URL + "breeds/image/random/" + str(num_of_img))
    data = json.loads(response.content)
    size_of_images = len(data["message"])

    assert size_of_images == num_of_img


def test_verify_all_breeds():
    response = requests.get(BASE_URL + "breeds/list/all")

    try:
        with open(JSON_FILE_LIST_DOGS, 'r') as file:
            exp_json = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{JSON_FILE_LIST_DOGS}' not found.")

    assert response.json() == exp_json
