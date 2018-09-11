import pytest
from store_requests.store import Store

store_manager = Store()

@pytest.mark.order1
def test_create_store():
    response_from_function = store_manager.create_store()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == store_manager.payload['id']

@pytest.mark.order2
def test_get_store_by_id():
    response_from_function = store_manager.get_store_by_id()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == store_manager.payload['id']

@pytest.mark.order3
def test_get_invalid_store_by_id():
    response_from_function = store_manager.get_invalid_store_by_id()
    assert response_from_function[1].status_code == 404
    # assert response_from_function[0]['id'] == store_manager.payload['id']

@pytest.mark.order4
def test_get_find_inventory_store():
    response_from_function = store_manager.get_store_inventory()
    assert response_from_function[1].status_code == 200

@pytest.mark.order5
def test_delete_store():
    """
    If store deleted - code responses = 404 ("Order not found")

    """
    response_from_function = store_manager.delete_store_by_id()
    assert response_from_function.status_code == 404





