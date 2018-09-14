import json

# from Test.test_data import url_site


# User_Object.create_user()
# User_Object.get_user_username()
# User_Object.update_user_username()
# User_Object.delete_user_username()
# from user_requests.usermanager import UserManager
# from user_requests.usermanager import UserManager
# from user_requests.usermanager import UserManager


class User:

    # user: dict = {}

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
# data = dict(user)
data_json = json.dumps(user.__dict__)
print(data_json)


# manager.create_user()
# manager.get_user_username()
# manager.update_user_username()
# manager.delete_user_username()




