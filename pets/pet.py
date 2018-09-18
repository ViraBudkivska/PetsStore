# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
import json


class Pet:
    """
    class: Class pet have fields
    """

    def __init__(self, id, category, name, photo_urls, tags, status):

        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photo_urls
        self.tags = tags
        self.status = status


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
DataJson = json.dumps(PetObject.__dict__)
