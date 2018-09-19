from Test.test_data import SUCCESS, store_inventory, data_json_for_store, store
import json
from Test.test_data import url_site
from store_requests.store_manager import StoreManager


manager = StoreManager(url_site)


def test_create_store():
    response_from_function = manager.create_store(data_json_for_store)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('id'), store.id
    assert json.loads(response_from_function.request.body.decode()).get('petId'), store.petId
    assert json.loads(response_from_function.request.body.decode()).get('quantity'), store.quantity
    assert json.loads(response_from_function.request.body.decode()).get('status'), store.status
    assert json.loads(response_from_function.request.body.decode()).get('complete'), store.complete


def test_get_store_by_id():
    response_from_function = manager.get_store_by_id(data_json_for_store)
    assert response_from_function.status_code == SUCCESS


def test_get_invalid_store_by_id():
    response_from_function = manager.get_invalid_store_by_id(data_json_for_store)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('id'), store.id


def test_get_find_inventory_store():
    response_from_function = manager.get_store_inventory(data_json_for_store)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()), json.loads(store_inventory.__dict__)


def test_delete_store():
    response_from_function = manager.delete_store_by_id(data_json_for_store)
    assert response_from_function.status_code == SUCCESS
