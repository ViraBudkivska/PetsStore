import json
import requests
import sys



class Pets:

    url = 'https://petstore.swagger.io/v2'
    payload = {
     "id": 1,
     "category": {
        "id": 2,
        "name": "Nimfa"
     },
     "name": "doggie",
     "photoUrls": [
        "https://www.what-dog.net/Images/faces2/scroll001.jpg"
        ],
     "tags": [
        {
            "id": 1,
            "name": "Hihi"
        }
        ],
     "status": "available"
    }

    # payload: dict = {}
    #
    # def __init__(self, **kwargs):
    #     """
    #
    #     :param kwargs:
    #     """
    #     self.payload = dict(**kwargs)
    #     self.url = _url

    def create_pet(self):
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

    def update_pet(self):
        self.payload['name'] = "Dog"
        self.payload['id'] = 123
        self.payload['status'] = "pending"
        response = requests.put(self.url + '/pet', json=self.payload)
        data = json.loads(response.text)
        return data, response

    def delete_pet_by_id(self):
        response = requests.delete(self.url + '/pet/' + str(self.payload['id']))
        # data = json.loads(response.text)
        return response

    def get_invalid_pet_by_id(self):
        self.payload['id'] = 6566565656
        response = requests.get(self.url + '/pet/' + str(self.payload['id']), json=self.payload)
        data = json.loads(response.text)
        return data, response


# category_dict = dict(id=12, name="Jojo")
# tag_dict = dict(id=45, name="HIHI")

# Pet_Object = Pets(id=1, category=category_dict, name="ZIZI", photoUrls="https://www.what-dog.net/Images/faces2/scroll001.jpg", tags=tag_dict,status="available")

# Pet_Object.create_pet()
# Pet_Object.get_pet_by_id()
# Pet_Object.get_find_by_status_pet()
# Pet_Object.update_pet()
# Pet_Object.delete_pet_by_id()
# Pet_Object.get_invalid_pet_by_id()

