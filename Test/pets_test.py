from pets.pet import Pet_Object

# pet_manager = Pets()


def test_create_pet():
    response_from_function = Pet_Object.create_pet()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == Pet_Object.payload['id']


def test_get_pet_by_id():
    response_from_function = Pet_Object.get_pet_by_id()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == Pet_Object.payload['id']


def test_get_find_by_status_pet():
    response_from_function = Pet_Object.get_find_by_status_pet()
    assert response_from_function[1].status_code == 200


def test_update_pet():
    response_from_function = Pet_Object.update_pet()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['name'] == Pet_Object.payload['name']
    assert response_from_function[0]['id'] == Pet_Object.payload['id']
    assert response_from_function[0]['status'] == Pet_Object.payload['status']


def test_delete_pet():
    response_from_function = Pet_Object.delete_pet_by_id()
    assert response_from_function.status_code == 200
    # assert response_from_function[0]['id'], response_from_function[1]['id']


def test_invalid_pet_by_id():
    response_from_function = Pet_Object.get_invalid_pet_by_id()
    assert response_from_function[1].status_code == 404


