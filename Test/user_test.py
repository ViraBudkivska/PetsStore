import pytest
from user_requests.user import User

user_manager = User()

@pytest.mark.order1
def test_create_user():
    response_from_function = user_manager.create_user()
    assert response_from_function.status_code == 200

@pytest.mark.order2
def test_get_user_username():
    response_from_function = user_manager.get_user_username()
    assert response_from_function.status_code == 200

@pytest.mark.order3
def test_update_user_username():
    response_from_function = user_manager.update_user_username()
    assert response_from_function.status_code == 200

@pytest.mark.order4
def test_delete_user_username():
    response_from_function = user_manager.delete_user_username()
    assert response_from_function.status_code == 200
