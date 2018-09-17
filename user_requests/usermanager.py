import json
import requests
from Test.test_data import new_username
from user_requests.user import user


class UserManager:

    def __init__(self, url):
        self.url = url

    def create_user(self, data_json):
        response = requests.post(self.url + '/user', json=json.loads(data_json))
        return response

    def get_user_username(self, data_json):
        response = requests.get(self.url + '/user/' + (json.loads(data_json)['username']), json=json.loads(data_json))
        return response

    def update_user_username(self, data_json):
        user.username = new_username
        response = requests.put(self.url + '/user/' + (json.loads(data_json)['username']), json=json.loads(data_json))
        return response

    def delete_user_username(self, data_json):
        response = requests.delete(self.url + '/user/' + (json.loads(data_json)['username']))
        return response




