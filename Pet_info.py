from enum import Enum
class StatusPets(Enum):
    available = 1
    pending = 2
    sold = 3
class Pet(object):

    swagger_types = {
        'id': 'int',
        'category': 'Category',
        'name': 'str',
        'photo_urls': 'list[str]',
        'tags': 'list[Tag]',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'name': 'name',
        'photo_urls': 'photoUrls',
        'tags': 'tags',
        'status': 'status'
    }
