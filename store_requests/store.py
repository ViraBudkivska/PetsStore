# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods


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



