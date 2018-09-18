# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
import json


class Store:
    """
    class: Store describe main field in store
    """

    def __init__(self, id, petId, quantity, ship_date, status, complete):
        self.id = id
        self.petId = petId
        self.quantity = quantity
        self.shipDate = ship_date
        self.status = status
        self.complete = complete


store = Store(id=12,
              petId=12,
              quantity=2,
              ship_date="2018-09-12T13:52:49.901Z",
              status="placed",
              complete=True)
data_json = json.dumps(store.__dict__)
