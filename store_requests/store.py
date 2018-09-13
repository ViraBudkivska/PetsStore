import requests
import json
# from Test.store_test import url_for_test


class Store:

    payload: dict = {}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        self.payload = dict(**kwargs)
        self.url = 'https://petstore.swagger.io/v2'

    def create_store(self):
        """ This function create store

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


Store_Object = Store(id=1, petId=1, quantity=2, shipDate="2018-09-12T13:52:49.901Z", status="placed", complete=True)

Store_Object.create_store()
Store_Object.get_store_inventory()
Store_Object.get_store_by_id()
Store_Object.get_invalid_store_by_id()
Store_Object.delete_store_by_id()




