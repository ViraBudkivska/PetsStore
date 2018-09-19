"""
module usermanager : have a class with methods
"""
# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
# pylint: disable=no-member
# pylint: disable=no-name-in-module
# pylint: disable=import-error

import json
import requests
from Test.test_data import new_username, user


class UserManager:
    """
    UserManager class that have main methods user
    """

    def __init__(self, url):
        self.url = url

    def create_user(self, data_json):
        """

        :param data_json:
        :return:
        """
        response = requests.post(self.url + '/user', json=json.loads(data_json))
        return response

    def get_user_username(self, data_json):
        """

        :param data_json:
        :return:
        """
        response = requests.get(self.url + '/user/' + (json.loads(data_json)['username']),
                                json=json.loads(data_json))
        return response

    def update_user_username(self, data_json):
        """

        :param data_json:
        :return:
        """
        user.username = new_username
        response = requests.put(self.url + '/user/' + (json.loads(data_json)['username']),
                                json=json.loads(data_json))
        return response

    def delete_user_username(self, data_json):
        """

        :param data_json:
        :return:
        """
        response = requests.delete(self.url + '/user/' + (json.loads(data_json)['username']))
        return response
