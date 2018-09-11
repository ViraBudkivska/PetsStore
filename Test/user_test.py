from user_requests.user import user_object

#user_manager = User()

def test_create_user():
    response_from_function = user_object.create_user()
    assert response_from_function.status_code == 200


def test_get_user_username():
    response_from_function = user_object.get_user_username()
    assert response_from_function.status_code == 200


def test_update_user_username():
    response_from_function = user_object.update_user_username()
    assert response_from_function.status_code == 200


def test_delete_user_username():
    response_from_function = user_object.delete_user_username()
    assert response_from_function.status_code == 200
