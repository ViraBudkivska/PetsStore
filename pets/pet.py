import json


class Pet:

    def __init__(self, id, category, name, photoUrls, tags, status):
        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status


category_dict = dict(id=12, name='Rex')
tag_dict = dict(id=123, name='Dog')
pet = Pet(id=55, category=category_dict, name="ZIZI", photoUrls=["https://www.what-dog.net/Images/faces2/scroll001.jpg"], tags=[tag_dict], status="available")
data_json = json.dumps(pet.__dict__)
