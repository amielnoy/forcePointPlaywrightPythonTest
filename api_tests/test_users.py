from api_tests.globals import ApiHttpConstants


def test_get_user_by_id(api):
    response = api.get("users/1")
    assert response.status_code == ApiHttpConstants.OK
    data = response.json()
    assert data["id"] == 1
    assert "username" in data

def test_get_user_by_id2(api):
    response = api.get("users/2")
    assert response.status_code == ApiHttpConstants.OK
    data = response.json()
    assert data["id"] == 2
    assert "username" in data

