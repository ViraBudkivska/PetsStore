import json


class Pet:

    def __init__(self, id, category, name, photoUrls, tags, status):
        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status


category_dict = dict(id=36, name='Rexy')
tag_dict = dict(id=4, name='Dog')
pet = Pet(id=456, category=category_dict, name="Xixi", photoUrls=["https://www.what-dog.net/Images/faces2/scroll001.jpg"], tags=[tag_dict], status='sold')
data_json = json.dumps(pet.__dict__)
