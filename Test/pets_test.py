from Test.test_data import NotFound, SUCCESS
from pets.pet import Pets

pet_manager = Pets()


def test_create_pet():
    response_from_function = pet_manager.create_pet()
    assert response_from_function[1].status_code == SUCCESS
    assert response_from_function[0]['id'] == pet_manager.payload['id']
    assert response_from_function[0]['category'] == pet_manager.payload['category']
    assert response_from_function[0]['photoUrls'] == pet_manager.payload['photoUrls']
    assert response_from_function[0]['tags'] == pet_manager.payload['tags']


def test_get_pet_by_id():
    response_from_function = pet_manager.get_pet_by_id()
    assert response_from_function[1].status_code == SUCCESS
    assert response_from_function[0]['id'] == pet_manager.payload['id']


def test_get_find_by_status_pet():
    response_from_function = pet_manager.get_find_by_status_pet()
    assert response_from_function[1].status_code == SUCCESS


def test_update_pet():
    response_from_function = pet_manager.update_pet()
    assert response_from_function[1].status_code == SUCCESS
    assert response_from_function[0]['name'] == pet_manager.payload['name']
    assert response_from_function[0]['id'] == pet_manager.payload['id']
    assert response_from_function[0]['status'] == pet_manager.payload['status']
    assert response_from_function[0]['category'] == pet_manager.payload['category']


def test_delete_pet():
    response_from_function = pet_manager.delete_pet_by_id()
    assert response_from_function.status_code == SUCCESS
    # assert response_from_function[0]['id'], response_from_function[1]['id']


def test_invalid_pet_by_id():
    response_from_function = pet_manager.get_invalid_pet_by_id()
    assert response_from_function[1].status_code == NotFound


