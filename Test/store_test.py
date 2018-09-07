from store_requests.store_info import Store

store_manager = Store()


def test_create_store():
    response_from_function = store_manager.create_store()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == store_manager.payload['id']


def test_get_store_by_id():
    response_from_function = store_manager.get_store_by_id()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == store_manager.payload['id']


def test_get_find_inventory_store():
    response_from_function = store_manager.get_store_inventory()
    assert response_from_function[1].status_code == 200


def test_delete_store():
    response_from_function = store_manager.delete_store_by_id()
    assert response_from_function[1].status_code == 200





