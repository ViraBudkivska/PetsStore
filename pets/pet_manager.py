import json
import requests

from Test.test_data import new_id, invalid_new_id
from pets.pet import pet


class PetManager:

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
        response = requests.get(self.url + '/pet/' + str(json.loads(data_json)['id']), json=json.loads(data_json))
        return response

    def get_find_by_status_pet(self, data_json):
        response = requests.get(self.url + '/pet/findByStatus?status=' + (json.loads(data_json)['status']), json=json.loads(data_json))
        return response

    def update_pet(self, data_json):
        pet.name = "Dog"
        pet.id = new_id
        pet.status = "pending"
        response = requests.put(self.url + '/pet', json=json.loads(data_json))
        return response

    def delete_pet_by_id(self, data_json):
        response = requests.delete(self.url + '/pet/' + str(json.loads(data_json)['id']))
        return response

    def get_invalid_pet_by_id(self, data_json):
        pet.id = invalid_new_id
        response = requests.get(self.url + '/pet/' + str(json.loads(data_json)['id']), json=json.loads(data_json))
        return response

