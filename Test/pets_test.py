from Test.test_data import SUCCESS, NotFound
import json
from Test.test_data import url_site
from pets.pet_manager import PetManager
from pets.pet import data_json, pet

manager = PetManager(url_site)


def test_create_pet():
    response_from_function = manager.create_pet(data_json)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('id'), pet.id
    assert json.loads(response_from_function.request.body.decode()).get('category'), pet.category
    assert json.loads(response_from_function.request.body.decode()).get('photoUrls'), pet.photoUrls
    assert json.loads(response_from_function.request.body.decode()).get('tags'), pet.tags


def test_get_pet_by_id():
    response_from_function = manager.get_pet_by_id(data_json)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('id'), pet.id


def test_get_find_by_status_pet():
    response_from_function = manager.get_find_by_status_pet(data_json)
    assert response_from_function.status_code == SUCCESS


def test_update_pet():
    response_from_function = manager.update_pet(data_json)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('name'), pet.name
    assert json.loads(response_from_function.request.body.decode()).get('id'), pet.id
    assert json.loads(response_from_function.request.body.decode()).get('status'), pet.status
    assert json.loads(response_from_function.request.body.decode()).get('category'), pet.category


def test_delete_pet():
    response_from_function = manager.delete_pet_by_id(data_json)
    assert response_from_function.status_code == SUCCESS


def test_invalid_pet_by_id():
    response_from_function = manager.get_invalid_pet_by_id(data_json)
    assert response_from_function.status_code == NotFound


