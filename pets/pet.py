import json
import requests

from Test.test_data import url_site, new_id, invalid_new_id


class Pets:

    # url = 'https://petstore.swagger.io/v2'
    # payload = {
    # "id": 1,
    # "category": {
    #    "id": 2,
    #    "name": "Nimfa"
    # },
    # "name": "doggie",
    # "photoUrls": [
    #    "https://www.what-dog.net/Images/faces2/scroll001.jpg"
    #    ],
    # "tags": [
    #    {
    #       "id": 1,
    #        "name": "Hihi"
    #    }
    #    ],
    # "status": "available"
    # }

    payload: dict = {}

    def __init__(self, **kwargs):
        self.url = url_site
        self.payload = dict(**kwargs)

    def create_pet(self, ):
        # payload = dict()
        response = requests.post(self.url + '/pet', json=self.payload)
        data = json.loads(response.text)
        return data, response

    def get_pet_by_id(self):
        response = requests.get(self.url + '/pet/' + str(self.payload['id']), json=self.payload)
        data = json.loads(response.text)
        return data, response

    def get_find_by_status_pet(self):
        response = requests.get(self.url + '/pet/findByStatus?status=available', json=self.payload)
        data = json.loads(response.text)
        return data, response

    def update_pet(self, pet):
        pet['name'] = "Dog"
        pet['id'] = new_id
        pet['status'] = "pending"
        response = requests.put(self.url + '/pet', json=self.payload)
        data = json.loads(response.text)
        return data, response

    def delete_pet_by_id(self):
        response = requests.delete(self.url + '/pet/' + str(self.payload['id']))
        return response

    def get_invalid_pet_by_id(self):
        self.payload['id'] = invalid_new_id
        response = requests.get(self.url + '/pet/' + str(self.payload['id']), json=self.payload)
        data = json.loads(response.text)
        return data, response


category_dict = dict(id=12, name="Jojo")
tag_dict = dict(id=45, name="HIHI")

Pet_Object = Pets(id=55, category=category_dict, name="ZIZI", photoUrls="https://www.what-dog.net/Images/faces2/scroll001.jpg", tags=tag_dict,status="available")

Pet_Object.create_pet()
Pet_Object.get_pet_by_id()
Pet_Object.get_find_by_status_pet()
Pet_Object.update_pet()
Pet_Object.delete_pet_by_id()
Pet_Object.get_invalid_pet_by_id()

