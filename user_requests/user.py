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
  "userStatus": 1
         }

    def create_user(self):
        response = requests.post(self.url + '/user', json=self.payload)
        return response

    def get_user_username(self):
        response = requests.get(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        return response



    def update_user_username(self):
        self.payload['username'] = "Nono"
        response = requests.put(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        return response

    def delete_user_username(self):
        response = requests.delete(self.url + '/user/' + str(self.payload['username']))
        return response

