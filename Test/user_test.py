# from Test.test_data import SUCCESS
from user_requests.user import manager

# user_manager = User()


def test_create_user():
    response_from_function = manager.create_user()
    assert response_from_function.status_code == 200


def test_get_user_username():
    response_from_function = manager.get_user_username()
    assert response_from_function.status_code == 200


def test_update_user_username():
    response_from_function = manager.update_user_username()
    assert response_from_function.status_code == 200


def test_delete_user_username():
    response_from_function = manager.delete_user_username()
    assert response_from_function.status_code == 200




