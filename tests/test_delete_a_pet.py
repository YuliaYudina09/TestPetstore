from base.base_test import BaseTest
import pytest
import conftest

class TestDeletePet(BaseTest):

    def test_delete_a_pet_ok(self, pet_create):
        id = pet_create

        response = self.petService.delete_a_pet(id)
        data = response.json()

        assert data["code"] == 200
        assert data["type"] == "unknown"
        assert data["message"] == str(id)
        
        assert response.status_code == 200

    def test_delete_a_pet_ivalid_id_not_found(self, pet_delete):
        id = pet_delete
        
        response = self.petService.delete_a_pet(id)
        assert response.status_code == 404

    @pytest.mark.parametrize(
            "id, expected_result",
            [
                (-1, 400),
                (0, 400),
                ("1", 400),
                ("abs", 400),
                (2.7, 400),
                (None, 400)
            ]
    )
    def test_delete_a_pet_invalid_id(self, id, expected_result, pet_create):

        id = pet_create

        response = self.petService.delete_a_pet(id)
        assert response.status_code == expected_result