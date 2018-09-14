# from Test.test_data import SUCCESS


# user_manager = User()
# from user_requests import user
from user_requests.usermanager import UserManager
from user_requests.user import data_json
from .test_data import url_site

manager = UserManager(url_site)
# print(data_json)

def test_create_user():
    response_from_function = manager.create_user(data_json)
    print(response_from_function)
    assert response_from_function[0]["id"] == data_json["id"]


# def test_get_user_username():
#     response_from_function = manager.get_user_username()
#     assert response_from_function.status_code == 200
#
#
# def test_update_user_username():
#     response_from_function = manager.update_user_username()
#     assert response_from_function.status_code == 200
#
#
# def test_delete_user_username():
#     response_from_function = manager.delete_user_username()
#     assert response_from_function.status_code == 200




