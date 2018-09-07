import requests
import json


class Pets:
    url = 'https://petstore.swagger.io/v2'
    payload = {'id': 1, 'category': {
        "id": 1,
        "name": "Horse"
    }, 'name': "PPUy", 'photoUrls': [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/" +
        "Biandintz_eta_zaldiak_-_modified2.jpg/1280px-Biandintz_eta_zaldiak_-_modified2.jpg"
    ], 'tags': [
        {
            "id": 6,
            "name": "BUBU"
        }
    ], 'status': "available"}



    def create_pet(self):
        response = requests.post(self.url + '/pet', json=self.payload)
        data = json.loads(response.text)
        return data, response


    def get_pet_by_id(self):
        response = requests.get(self.url + '/pet/' + str(self.payload['id'][id]), json=self)
        return response

    def get_find_by_status_pet(self):
        response = requests.get(self.url + '/pet/findByStatus?status=available', json=self.payload)
        data = json.loads(response.text)
        return data, response


    def update_pet(self):
        self.payload['name'] = "Dog"
        self.payload['id'] = "123"
        self.payload['status'] = "pending"
        response = requests.put(self.url + '/pet', json=self)
        data = json.loads(response.text)
        return data, response


    def delete_pet_by_id(self):
        response = requests.delete(self.url + '/pet/' + str(self.payload['id']), json=self)
        data = json.loads(response.text)
        return data, response

