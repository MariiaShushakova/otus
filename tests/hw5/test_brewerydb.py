import json
import requests
import pytest

BASE_URL = "https://api.openbrewerydb.org/v1/breweries/"


def test_validate_statuscode():
    response = requests.get(BASE_URL + "random")
    assert response.status_code == 200, "Wrong status code" + str(response.status_code)


def test_invalidate_statuscode():
    invalid_response = requests.get(BASE_URL + "12345")
    assert invalid_response.status_code == 404, "Expected 404 status code" + str(invalid_response.status_code)


def test_validate_size():
    response = requests.get(BASE_URL + "random?size=5")
    data = json.loads(response.content)
    size = len(data)

    assert size == 3


@pytest.mark.parametrize("ex_city",
                         ["Worcester", "Cincinnati", "Austintown"])
def test_request_by_city(ex_city):
    response = requests.get(BASE_URL + "?by_city=" + ex_city)
    data = json.loads(response.content)

    for item in data:
        ac_city = item.get("city")
        if ac_city is not None:
            assert ac_city == ex_city


@pytest.mark.parametrize(("total", "country"),
                         [(61, "south_korea"),
                         (7967, "united_states"),
                         (0, "german")])
def test_total_by_country(total, country):
    response = requests.get(BASE_URL + "meta?by_country=" + country)
    data = json.loads(response.content)

    assert data["total"] == str(total)

