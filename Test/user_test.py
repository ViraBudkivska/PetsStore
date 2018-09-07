from user_requests.user_info import User

user_manager = User()


def test_create_user():
    response_from_function = user_manager.create_user()
    assert response_from_function[0].status_code == 200
    # assert response_from_function[0]['id'] == user_manager.payload['id']

def test_get_user_login():
    response_from_function = user_manager.get_user_login()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['username'] == user_manager.payload['username']


def test_get_user_username():
    response_from_function = user_manager.get_user_username()
    assert response_from_function[1].status_code == 200


def test_update_pet():
    response_from_function = user_manager.update_user_username()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['name'], response_from_function[1]['name']
    assert response_from_function[0]['id'], response_from_function[1]['id']
    assert response_from_function[0]['status'], response_from_function[1]['status']


def test_delete_pet():
    response_from_function = user_manager.delete_user_username()
    assert response_from_function[1].status_code == 200