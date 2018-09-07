from store_requests.store_info import Store

pet_manager = Store()


def test_create_store():
    response_from_function = pet_manager.create_store()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == pet_manager.payload['id']


def test_get_store_by_id():
    response_from_function = pet_manager.get_store_by_id()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == pet_manager.payload['id']


def test_get_find_inventory_store():
    response_from_function = pet_manager.get_store_inventory()
    assert response_from_function[1].status_code == 200


def test_delete_pet():
    response_from_function = pet_manager.delete_pet_by_id()
    assert response_from_function[1].status_code, 200
    assert response_from_function[0]['id'], response_from_function[1]['id']





