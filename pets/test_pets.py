import json
import requests

from pets.pet_info import Pets

pet_manager = Pets()


def test_create_pet():
    response = pet_manager.create_pet()
    assert response[1].status_code == 200
    assert response[0]['id'] == pet_manager.payload['id']


def test_get_pet_by_id():
     response = pet_manager.
     assert response.status_code, 200
     assert data['name'], self.payload['name']


# def test_get_find_by_status_pet(self):
#     response = requests.get(self.url + '/pet/findByStatus?status=available', json=self.payload)
#     assert response.status_code, 200
#
#
# def test_update_pet(self):
#     self.payload['name'] = "Dog"
#     self.payload['id'] = "123"
#     self.payload['status'] = "pending"
#     response = requests.put(self.url + '/pet', json=self.payload)
#     assert response.status_code, 200
#     data = json.loads(response.text)
#     assert data['name'], self.payload['name']
#     assert data['id'], self.payload['id']
#     assert data['status'], self.payload['status']
#
#
# def test_в_pet(self):
#     response = requests.post(self.url + '/pet', json=self.payload)
#     assert response.status_code, 200
#     data = json.loads(response.text)
#     assert data['id'], self.payload['id']
