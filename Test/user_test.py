from user_requests.usermanager import User_Object


# user_manager = User()

def test_create_user():
    response_from_function = User_Object.create_user()
    assert response_from_function.status_code == 200


def test_get_user_username():
    response_from_function = User_Object.get_user_username()
    assert response_from_function.status_code == 200


def test_update_user_username():
    response_from_function = User_Object.update_user_username()
    assert response_from_function.status_code == 200


def test_delete_user_username():
    response_from_function = User_Object.delete_user_username()
    assert response_from_function.status_code == 200


