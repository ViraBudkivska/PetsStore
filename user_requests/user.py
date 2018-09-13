import requests
import sys

from Test.test_data import url_site, new_username, error_message


class User:

    payload: dict = {}

    def __init__(self, **kwargs):
        self.payload = dict(**kwargs)
        self.url = url_site

    def create_user(self):
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


