"""
Module:
"""
# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
# pylint: disable=no-member
# pylint: disable=no-name-in-module
# pylint: disable=import-error
import json
import requests

import Test.test_data
from pets.pet import PetObject


class PetManager:
    """
    class: PetManager describe main methods
    """

    def __init__(self, url):
        """
        :param url: -- url site which testing
        """
        self.url = url

    def create_pet(self, data_json):
        """
        :param data_json:  -- param which have a pet object converted in dictionary type
        :return: response:  -- the return code
        """
        response = requests.post(self.url + '/pet', json=json.loads(data_json))
        return response

    def get_pet_by_id(self, data_json):
        """

        :param data_json:
        :return:
        """
        response = requests.get(self.url + '/pet/' + str(json.loads(data_json)['id']),
                                json=json.loads(data_json))
        return response

    def get_find_by_status_pet(self, data_json):
        """

        :param DataJson:
        :return:
        """
        response = requests.get(self.url + '/pet/findByStatus?status='
                                + (json.loads(data_json)['status']),
                                json=json.loads(data_json))
        return response

    def update_pet(self, data_json):
        """

        :param DataJson:
        :return:
        """
        PetObject.name = "Dog"
        PetObject.id = Test.test_data.new_id
        PetObject.status = "pending"
        response = requests.put(self.url + '/pet', json=json.loads(data_json))
        return response

    def delete_pet_by_id(self, data_json):
        """

        :param DataJson:
        :return:
        """
        response = requests.delete(self.url + '/pet/' + str(json.loads(data_json)['id']))
        return response

    def get_invalid_pet_by_id(self, data_json):
        """

        :param DataJson:
        :return:
        """
        PetObject.id = Test.test_data.invalid_new_id
        response = requests.get(self.url + '/pet/' + str(json.loads(data_json)['id']),
                                json=json.loads(data_json))
        return response
