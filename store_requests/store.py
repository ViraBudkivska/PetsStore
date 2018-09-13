import requests
import json
# from Test.store_test import url_for_test
from Test.test_data import url_site


class Store:

    payload: dict = {}

    def __init__(self, **kwargs):
        self.payload = dict(**kwargs)
        self.url = url_site

    def create_store(self):
        """
        This function create store

        :return:    data, response -- the return code
        """
        response = requests.post(self.url + '/store/order', json=self.payload)
        data = json.loads(response.text)
        return data, response

    def get_store_inventory(self):
        """ This function get information about store inve

        :return:    data, response -- the return code
        """
        response = requests.get(self.url + '/store/inventory', json=self.payload)
        data = json.loads(response.text)
        return data, response

    def get_store_by_id(self):
        """ This function get information about store by id

        :return:    data, response -- the return code
        """
        response = requests.get(self.url + '/store/order/' + str(self.payload['id']), json=self.payload)
        data = json.loads(response.text)
        return data, response

    def get_invalid_store_by_id(self):
        """ Try to get information about story by id

        :return:    data, response -- the return code
        """
        self.payload['id'] = 123
        response = requests.get(self.url + '/store/order/' + str(self.payload['id']), json=self.payload)
        data = json.loads(response.text)
        return data, response

    def delete_store_by_id(self):
        """ This function delete store by id

        :return:    response -- the return code
        """
        response = requests.delete(self.url + '/store/order/' + str(self.payload['id']))
        return response






