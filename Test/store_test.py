import pytest
from store_requests.store import Store_Object

# store_manager = Store()
# url_for_test = 'https://petstore.swagger.io/v2'


def test_create_store():
    response_from_function = Store_Object.create_store()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == Store_Object.payload['id']
    assert response_from_function[0]['petId'] == Store_Object.payload['petId']
    assert response_from_function[0]['quantity'] == Store_Object.payload['quantity']
    assert response_from_function[0]['status'] == Store_Object.payload['status']
    assert response_from_function[0]['complete'] == Store_Object.payload['complete']


def test_get_store_by_id():
    response_from_function = Store_Object.get_store_by_id()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == Store_Object.payload['id']


def test_get_invalid_store_by_id():
    response_from_function = Store_Object.get_invalid_store_by_id()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == Store_Object.payload['id']


def test_get_find_inventory_store():
    response_from_function = Store_Object.get_store_inventory()
    assert response_from_function[1].status_code == 200


def test_delete_store():
    response_from_function = Store_Object.delete_store_by_id()
    assert response_from_function.status_code == 200





