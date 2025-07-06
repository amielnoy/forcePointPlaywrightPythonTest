from api_tests.globals import ApiHttpConstants


def test_get_user_by_id(api):
    response = api.get("users/1")
    assert response.status_code == ApiHttpConstants.OK
    data = response.json()
    assert data["id"] == 1
    assert "username" in data

def test_create_post(api):
    payload = {
        "userId": 1,
        "title": "New test post",
        "body": "This is a body of the test post"
    }
    response = api.post("posts", data=payload)
    assert response.status_code == ApiHttpConstants.CREATED
    data = response.json()
    assert data["title"] == payload["title"],"data <> payload!"

def test_update_post(api):
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }
    response = api.put("posts/1", data=payload)
    assert response.status_code == ApiHttpConstants.OK
    assert response.json()["title"] == "Updated title"

def test_delete_post(api):
    response = api.delete("posts/1")
    assert response.status_code == ApiHttpConstants.OK
