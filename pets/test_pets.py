import json
import requests

# from pets.pet_info import Pets
#
# pet_manager = Pets()


# def test_create_pet():
#     response_from_function = pet_manager.create_pet()
#     assert response_from_function[1].status_code == 200
#     assert response_from_function[0]['id'] == pet_manager.payload['id']
#
#
# def test_get_pet_by_id():
#     response_from_function = pet_manager.get_pet_by_id()
#     assert response_from_function[1].status_code == 200
#     assert response_from_function[0]['id'] == pet_manager.payload['id']
#
#
# def test_get_find_by_status_pet(self):
#     response_from_function = pet_manager.get_find_by_status_pet()
#     assert response_from_function[0].status_code, 200
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
