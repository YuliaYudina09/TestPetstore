from base.base_test import BaseTest
from services.pet_service.models.model import PetModel
import pytest
import conftest

class TestFindPetById(BaseTest):

    def test_find_pet_by_id_ok(self, pet_create):
        id = pet_create
        response = self.petService.find_pet_by_id(id)

        data = response.json()
        if data != None:
            PetModel(**data)
            assert data["id"] == id 
               
        assert response.status_code == 200

    def test_find_pet_by_id_ivalid_id_not_found(self, pet_delete):
        id = pet_delete
        response = self.petService.find_pet_by_id(id)

        data = response.json()

        assert data["code"] == 1
        assert data["type"] == "error"
        assert data["message"] == "Pet not found"

        assert response.status_code == 404

    @pytest.mark.parametrize(
            "id",
            [
                (None),
                ("abcde"),
                (-1),
                (2.5),
                (0)
            ]
    )
    def test_find_pet_by_ivalid_id(self, id):
        response = self.petService.find_pet_by_id(id)  
        assert response.status_code == 400

    

