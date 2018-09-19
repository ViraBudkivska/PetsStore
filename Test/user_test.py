from Test.test_data import SUCCESS, data_json_for_user, user
import json
from Test.test_data import url_site
from user_requests.usermanager import UserManager


manager = UserManager(url_site)


def test_create_user():
    response_from_function = manager.create_user(data_json_for_user)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('id'), user.id


def test_get_user_username():
    response_from_function = manager.get_user_username(data_json_for_user)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('username'), user.username


def test_update_user_username():
    response_from_function = manager.update_user_username(data_json_for_user)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('username'), user.username


def test_delete_user_username():
    response_from_function = manager.delete_user_username(data_json_for_user)
    assert response_from_function.status_code == SUCCESS
