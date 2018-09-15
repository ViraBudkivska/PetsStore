import json

import requests
# import sys
# import json

from Test.test_data import url_site
# from user_requests import user
# from user_requests.user import User


class UserManager:

    def __init__(self, url):
        self.url = url

    def create_user(self, data_user):
        return requests.post(self.url + '/user', json=json.loads(data_user))



    # def get_user_username(self, user: User):
    #     response = requests.get(user.url + '/user/' + user.username, json=user.get_data())
    #     return response
    #
    # def update_user_username(self, user: User):
    #     self.payload['username'] = new_username
    #     response = requests.put(user.url + '/user/' + user.username, json=user.get_data())
    #     return response
    #
    # def delete_user_username(self, user: User):
    #     response = requests.delete(user.url + '/user/' + user.username)
    #     try:
    #         if response.status_code == 200:
    #             return response
    #     except Exception:
    #         print(error_message)
    #         print(sys.exc_info())
    #         exit()



