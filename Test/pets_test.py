import json
import requests

from pets.pet_info import Pets


def test_create_pet(self):
    assert create_pet.response.status_code, 200
    data = json.loads(response.text)
    assert data['id'], self.payload['id']




