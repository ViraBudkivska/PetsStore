from pets.pet import pet_object

#pet_manager = Pets()


def test_create_pet():
    response_from_function = pet_object.create_pet()
    # assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == response_from_function[1][id]


def test_get_pet_by_id():
    response_from_function = pet_object.get_pet_by_id()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['id'] == pet_object.payload['id']


def test_get_find_by_status_pet():
    response_from_function = pet_object.get_find_by_status_pet()
    assert response_from_function[1].status_code == 200


def test_update_pet():
    response_from_function = pet_object.update_pet()
    assert response_from_function[1].status_code == 200
    assert response_from_function[0]['name'], response_from_function[1]['name']
    assert response_from_function[0]['id'], response_from_function[1]['id']
    assert response_from_function[0]['status'], response_from_function[1]['status']


def test_delete_pet():
    response_from_function = pet_object.delete_pet_by_id()
    assert response_from_function.status_code == 200
    # assert response_from_function[0]['id'], response_from_function[1]['id']


def test_invalid_pet_by_id():
    response_from_function = pet_object.get_invalid_pet_by_id()
    assert response_from_function[1].status_code == 404


