# pylint: disable=too-many-arguments
from Test.test_data import SUCCESS
import json
from Test.test_data import url_site
from user_requests.usermanager import UserManager
from user_requests.user import data_json, user

manager = UserManager(url_site)


def test_create_user():
    response_from_function = manager.create_user(data_json)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('id'), user.id


def test_get_user_username():
    response_from_function = manager.get_user_username(data_json)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('username'), user.username


def test_update_user_username():
    response_from_function = manager.update_user_username(data_json)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('username'), user.username


def test_delete_user_username():
    response_from_function = manager.delete_user_username(data_json)
    assert response_from_function.status_code == SUCCESS




