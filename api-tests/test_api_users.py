# test_api_users.py
import requests

def test_get_users_list():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()

    assert "data" in data
    assert len(data["data"]) > 0
    assert data["data"][0]["email"].endswith("@reqres.in")
