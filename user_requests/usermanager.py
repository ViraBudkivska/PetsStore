import requests
import sys
import json

from Test.test_data import url_site, new_username, error_message
from user_requests.user import user_1


class UserManager:

    payload = json.dumps(user_1)
    user_1: dict = {}

    def __init__(self, **kwargs):
        self.url = url_site
        self.payload = dict(**kwargs)

    def create_user(self):
        # payload = dict(**user)
        response = requests.post(self.url + '/user', json=self.payload)
        try:
            if response.status_code == 200:
                return response
        except Exception:
            print(error_message)
            print(sys.exc_info())
            exit()

    def get_user_username(self):
        response = requests.get(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        return response

    def update_user_username(self):
        self.payload['username'] = new_username
        response = requests.put(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        return response

    def delete_user_username(self):
        response = requests.delete(self.url + '/user/' + str(self.payload['username']))
        try:
            if response.status_code == 200:
                return response
        except Exception:
            print(error_message)
            print(sys.exc_info())
            exit()


class User:
    # id = int
    # username = str
    # firstName = str
    # lastName = str
    # email = str
    # password = str
    # phone = str
    # userStatus = int

    def __init__(self, id, username, firstName, lastName, email, password, phone, userStatus):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus
