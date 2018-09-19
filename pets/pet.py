# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
# import json


class Pet:
    """
    class: Class Pet contains all the fields needed to create an object
    """

    def __init__(self, id, category, name, photo_urls, tags, status):

        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photo_urls
        self.tags = tags
        self.status = status
