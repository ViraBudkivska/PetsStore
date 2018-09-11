import pytest
from pets.pet import Pets

pet_manager = Pets()

@pytest.mark.order1
def test_create_pet():
    response_from_function = pet_manager.create_pet()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == pet_manager.payload['id']

@pytest.mark.order2
def test_get_pet_by_id():
    response_from_function = pet_manager.get_pet_by_id()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == pet_manager.payload['id']

@pytest.mark.order3
def test_get_find_by_status_pet():
    response_from_function = pet_manager.get_find_by_status_pet()
    assert response_from_function[1].status_code == 200

@pytest.mark.order4
def test_update_pet():
    response_from_function = pet_manager.update_pet()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['name'], response_from_function[1]['name']
    assert response_from_function[0]['id'], response_from_function[1]['id']
    assert response_from_function[0]['status'], response_from_function[1]['status']

@pytest.mark.order5
def test_delete_pet():
    response_from_function = pet_manager.delete_pet_by_id()
    assert response_from_function.status_code == 200
    # assert response_from_function[0]['id'], response_from_function[1]['id']

@pytest.mark.order6
def test_invalid_pet_by_id():
    response_from_function = pet_manager.get_invalid_pet_by_id()
    assert response_from_function[1].status_code == 404


