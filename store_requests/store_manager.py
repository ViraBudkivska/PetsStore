"""
store_manager :
"""
# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
# pylint: disable=no-member
# pylint: disable=no-name-in-module
# pylint: disable=import-error
import json
import requests

from Test.test_data import new_id, store


class StoreManager:
    """
    Store Manager describe main methods with store
    """

    def __init__(self, url):
        self.url = url

    def create_store(self, data_json):
        """
        This function create store

        :return:   response -- the return code
        """
        response = requests.post(self.url + '/store/order', json=json.loads(data_json))
        return response

    def get_store_inventory(self, data_json):
        """ This function get information about store inve

        :return:   response -- the return code
        """
        response = requests.get(self.url + '/store/inventory', json=json.loads(data_json))
        return response

    def get_store_by_id(self, data_json):
        """ This function get information about store by id

        :return:    response -- the return code
        """
        response = requests.get(self.url + '/store/order/' + str(json.loads(data_json)['id']),
                                json=json.loads(data_json))
        return response

    def get_invalid_store_by_id(self, data_json):
        """ Try to get information about story by id

        :return:    response -- the return code
        """
        store.id = new_id
        response = requests.get(self.url + '/store/order/' + str(json.loads(data_json)['id']),
                                json=json.loads(data_json))
        return response

    def delete_store_by_id(self, data_json):
        """ This function delete store by id

        :return:    response -- the return code
        """
        response = requests.delete(self.url + '/store/order/' + str(json.loads(data_json)['id']))
        return response
