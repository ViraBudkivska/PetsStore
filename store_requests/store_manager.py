from store_requests.store import Store

Store_Object = Store(id=1, petId=1, quantity=2, shipDate="2018-09-12T13:52:49.901Z", status="placed", complete=True)

Store_Object.create_store()
Store_Object.get_store_inventory()
Store_Object.get_store_by_id()
Store_Object.get_invalid_store_by_id()
Store_Object.delete_store_by_id()
