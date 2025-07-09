from api_tests.globals import ApiHttpConstants


def test_get_posts_count(api):
    response = api.get("posts")
    assert response.status_code == ApiHttpConstants.OK
    data = response.json()
    assert len(data) == 100

def test_get_post_number1(api):
    response = api.get("posts/1")
    assert response.status_code == ApiHttpConstants.OK
    data = response.json()
    assert data['userId'] == 1,"error in user id,expected 1"
    assert data['id'] == 1,"error is user id,expected 1"
    assert data['title'] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit","eror in title"
    assert data['body'] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto","erorr in body"

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
