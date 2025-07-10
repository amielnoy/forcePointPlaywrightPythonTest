from api_tests.globals import ApiHttpConstants


def test_get_posts_count(api):
    response = api.get("users/1/albums")
    assert response.status_code == ApiHttpConstants.OK
    data = response.json()
    assert len(data) == 10

def test_get_user_albom_number_2(api):
    response = api.get("users/1/albums")
    assert response.status_code == ApiHttpConstants.OK
    data = response.json()
    assert data[2]['userId'] == 1,"error in user id,expected 3"
    assert data[2]['id'] == 3,"error is user id,expected 3"
    assert data[2]['title'] == "omnis laborum odio"
