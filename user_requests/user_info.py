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
        # data = json.loads(response.text)
        return response


    def get_user_username(self):
        response = requests.get(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        data = json.loads(response.text)
        return data, response

    def get_user_login(self):
        response = requests.get(self.url + 'user/login?username=Nini&password=123456', json=self.payload)
        # data = json.loads(response.text)
        return response


    def update_user_username(self):
        self.payload['id'] = "666"
        self.payload['phone'] = "12565254325163"
        self.payload['lastName'] = "Jira"
        response = requests.put(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        data = json.loads(response.text)
        return data, response


    def delete_user_username(self):
        response = requests.delete(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        data = json.loads(response.text)
        return data, response

