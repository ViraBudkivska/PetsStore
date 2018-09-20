"""
module: Pets test
"""
import json
from Test.test_data import SUCCESS, NotFound, PetObject, DataJsonForPets, url_site
from pets.pet_manager import PetManager

manager = PetManager(url_site)


def test_create_pet():
    """
    :return:
    """
    response_from_function = manager.create_pet(DataJsonForPets)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('id'), PetObject.id
    assert json.loads(response_from_function.request.body.decode()).get('category'), \
        PetObject.category
    assert json.loads(response_from_function.request.body.decode()).get('photoUrls'),\
        PetObject.photoUrls
    assert json.loads(response_from_function.request.body.decode()).get('tags'), PetObject.tags


def test_get_pet_by_id():
    """
    :return:
    """
    response_from_function = manager.get_pet_by_id(DataJsonForPets)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('id'), PetObject.id


def test_get_find_by_status_pet():
    """
    :return:
    """
    response_from_function = manager.get_find_by_status_pet(DataJsonForPets)
    assert response_from_function.status_code == SUCCESS


def test_update_pet():
    """
    :return:
    """
    response_from_function = manager.update_pet(DataJsonForPets)
    assert response_from_function.status_code == SUCCESS
    assert json.loads(response_from_function.request.body.decode()).get('name'), PetObject.name
    assert json.loads(response_from_function.request.body.decode()).get('id'), \
        PetObject.id
    assert json.loads(response_from_function.request.body.decode()).get('status'), PetObject.status
    assert json.loads(response_from_function.request.body.decode()).get('category'),\
        PetObject.category


def test_delete_pet():
    """
    :return:
    """
    response_from_function_first_step = manager.create_pet(DataJsonForPets)
    response_from_function = manager.delete_pet_by_id(DataJsonForPets)
    assert response_from_function.status_code, response_from_function_first_step == SUCCESS


def test_invalid_pet_by_id():
    """
    :return:
    """
    response_from_function = manager.get_invalid_pet_by_id(DataJsonForPets)
    assert response_from_function.status_code == NotFound
