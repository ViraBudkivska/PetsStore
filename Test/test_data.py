import json

from pets.pet import Pet
from store_requests.store import Store
from user_requests.user import User

SUCCESS = 200
NotFound = 404
url_site = 'https://petstore.swagger.io/v2'
new_username = "Khrystyna"
new_id = 12345
invalid_new_id = 1234
error_message = "oops we have a problem!"
store_inventory = {
  "1": 1,
  "4444": 2,
  "teste": 1,
  "string": 6738,
  "Operated": 4,
  "pending": 56,
  "Not-Operated": 10,
  "available": 4800,
  "waiting list": 1,
  "Unavailable": 1,
  "Shortlisted": 1,
  "Sold": 1,
  "availasdfsadfasdfble": 1,
  "not available": 1,
  "Available": 1,
  "YAI3424forYAI3373": 1,
  "ok": 1,
  "KBMAvailable": 3,
  "onwork": 1,
  "sold": 87,
  "ddd": 1,
  "Nonavailable": 1,
  "Offline": 1,
  "straight": 2,
  "pendin": 1,
  "sts": 1,
  "onhold": 3,
  "status": 5,
  "xavailable": 1
}

Category_Dict = dict(id=36,
                     name='Rexy')
tag_dict = dict(id=4,
                name='Dog')
PetObject = Pet(id=456,
                category=Category_Dict,
                name="Xixi",
                photo_urls=["https://www.what-dog.net/Images/faces2/scroll001.jpg"],
                tags=[tag_dict],
                status='sold')
DataJsonForPets = json.dumps(PetObject.__dict__)

store = Store(id=12,
              petId=12,
              quantity=2,
              ship_date="2018-09-12T13:52:49.901Z",
              status="placed",
              complete=True)
data_json_for_store = json.dumps(store.__dict__)

user = User(id=3,
            username="Nini",
            first_name="Vira",
            last_name="Budda",
            email="email@gmail.com",
            password="1234567",
            phone="55455545",
            user_status=1)
data_json_for_user = json.dumps(user.__dict__)
