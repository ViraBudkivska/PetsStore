import requests
import sys
import json

# class User:
#
#     payload = {
#   "id": 1,
#   "username": "Nini",
#   "firstName": "Lidiya",
#   "lastName": "Kozak",
#   "email": "nini@gfnnf.com",
#   "password": "123456",
#   "phone": "0967667575",
#   "userStatus": 1
#          }


class User:

    payload: dict = {}

    def __init__(self, **kwargs):
        self.payload = dict(**kwargs)
        self.url = 'https://petstore.swagger.io/v2'

    def create_user(self):
        response = requests.post(self.url + '/user', json=self.payload)
        try:
            if response.status_code == 200:
                return response
        except Exception:
            print("oops we have a problem!")
            print(sys.exc_info())
            exit()

    def get_user_username(self):
        response = requests.get(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        return response

    def update_user_username(self):
        self.payload['username'] = "Nono"
        response = requests.put(self.url + '/user/' + str(self.payload['username']), json=self.payload)
        return response

    def delete_user_username(self):
        response = requests.delete(self.url + '/user/' + str(self.payload['username']))
        try:
            if response.status_code == 200:
                return response
        except Exception:
            print("oops we have a problem!")
            print(sys.exc_info())
            exit()


User_Object = User(id=1, username="Ninih", firstName="Vira", lastName="Budda", email="email@gmail.com", password="1234567", phone="55455545", userStatus=0)

User_Object.create_user()
User_Object.get_user_username()
User_Object.update_user_username()
User_Object.delete_user_username()