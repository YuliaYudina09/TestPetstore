import pytest
from services.pet_service import pet_service

@pytest.fixture
def pet_delete():

    id_for_delete = 123

    petService = pet_service.PetService()
    petService.delete_a_pet(id_for_delete)

    return id_for_delete

@pytest.fixture
def pet_create():
    petService = pet_service.PetService()
    payload = petService.payloads.add_a_new_pet
    payload["id"] = 555
    petService.add_a_new_pet(payload)

    return payload["id"]
