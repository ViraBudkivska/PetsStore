import json


class User:

    def __init__(self, id, username, firstName, lastName, email, password, phone, userStatus):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus


user = User(id=3, username="Nini", firstName="Vira", lastName="Budda", email="email@gmail.com", password="1234567", phone="55455545", userStatus=1)
data_json = json.dumps(user.__dict__)






