import requests
import json


class User:
    url = 'https://petstore.swagger.io/v2'
    payload = {
  "id": 1,
  "username": "Nini",
  "firstName": "Lidiya",
  "lastName": "Kozak",
  "email": "nini@gfnnf.com",
  "password": "123456",
  "phone": "0967667575",
  "userStatus": 0
}

    def create_user(self):
        response = requests.post(self.url + '/user', json=self.payload)
        data = json.loads(response.text)
        return data, response


    def get_user_username(self):
        response = requests.get(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        data = json.loads(response.text)
        return data, response

    def get_user_login(self):
        response = requests.get(self.url + '/pet/findByStatus?status=available', json=self.payload)
        data = json.loads(response.text)
        return data, response


    def update_user_username(self):
        self.payload['name'] = "Dog"
        self.payload['id'] = "123"
        self.payload['status'] = "pending"
        response = requests.put(self.url + '/pet', json=self.payload)
        data = json.loads(response.text)
        return data, response


    def delete_user_username(self):
        response = requests.delete(self.url + '/pet/' + str(self.payload['id']), json=self.payload)
        data = json.loads(response.text)
        return data, response

