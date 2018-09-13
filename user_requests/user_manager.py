from user_requests.user import User

User_Object = User(id=1, username="Ninih", firstName="Vira", lastName="Budda", email="email@gmail.com", password="1234567", phone="55455545", userStatus=0)

User_Object.create_user()
User_Object.get_user_username()
User_Object.update_user_username()
User_Object.delete_user_username()