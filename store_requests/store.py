import json


class Store:

    def __init__(self, id, petId, quantity, shipDate, status, complete):
        self.id = id
        self.petId = petId
        self.quantity = quantity
        self.shipDate = shipDate
        self.status = status
        self.complete = complete


store = Store(id=12, petId=12, quantity=2, shipDate="2018-09-12T13:52:49.901Z", status="placed", complete=True)
data_json = json.dumps(store.__dict__)
