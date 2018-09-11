import requests
import json


class Store:
    url = 'https://petstore.swagger.io/v2'
    payload = {
  "id": 1,
  "petId": 1,
  "quantity": 1,
  "shipDate": "",
  "status": "placed",
  "complete": False
               }


    def create_store(self):
        """

        :return: data response
        """
        response = requests.post(self.url + '/store/order', json=self.payload)
        data = json.loads(response.text)
        return data, response


    def get_store_inventory(self):
        response = requests.get(self.url + '/store/inventory', json=self.payload)
        data = json.loads(response.text)
        return data, response


    def get_store_by_id(self):
        response = requests.get(self.url + '/store/order/' + str(self.payload['id']), json=self.payload)
        data = json.loads(response.text)
        return data, response

    def get_invalid_store_by_id(self):
        self.payload['id'] = 123
        response = requests.get(self.url + '/store/order/' + str(self.payload['id']), json=self.payload)
        data = json.loads(response.text)
        return data, response


    def delete_store_by_id(self):
        response = requests.delete(self.url + '/store/order/' + str(self.payload['id']))
        return response


