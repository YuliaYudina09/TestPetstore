from base.base_test import BaseTest
from services.pet_service.models.model import PetModel
import pytest
import conftest

class TestUpdatePetWithData(BaseTest):

    def test_update_a_pet_with_data_ok(self, pet_create):
        id = pet_create
        name = "Rick"
        status = "available"
        response = self.petService.update_a_pet_with_form_data(id, name, status)
        
        data = self.petService.find_pet_by_id(id).json()
        assert data["name"] == name
        assert data["status"] == status
        
        assert response.status_code == 200

    @pytest.mark.parametrize(
            "id, name, status, expected_result",
            {
                (555, "Max", "available", 405),
                ("abcde", "Max", "available", 405),
                (-1, "Max", "available", 405),
                (2.5, "Max", "available", 405),
                (0, "Max", "available", 405),
                (None, "Max", "available", 405)
            }
    )
    def test_update_a_pet_with_data_ivalid_id(self, id, name, status, expected_result):
        response = self.petService.update_a_pet_with_form_data(id, name, status)  
        assert response.status_code == expected_result

    @pytest.mark.parametrize(
            "name, status, expected_result",
            {
                (123456, "available", 405),
                (2.5, "available", 405)
            }
    )
    def test_update_a_pet_with_data_ivalid_name(self, name, status, pet_create, expected_result):
        id = pet_create
        response = self.petService.update_a_pet_with_form_data(id, name, status)  
        assert response.status_code == expected_result

    @pytest.mark.parametrize(
            "name, status, expected_result",
            {
                ("Max", 12345, 405),
                ("Max", 2.5, 405)
            }
    )
    def test_update_a_pet_with_data_ivalid_status(self, name, status, pet_create, expected_result):
        id = pet_create
        response = self.petService.update_a_pet_with_form_data(id, name, status)  
        assert response.status_code == expected_result
    

    

