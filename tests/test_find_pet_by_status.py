from base.base_test import BaseTest
from services.pet_service.models.model import PetModel
import pytest

class TestFindPetByStatus(BaseTest):

    @pytest.mark.parametrize(
            "status, expected_result",
            [
                (["available"], 200),
                (["pending"], 200),
                (["sold"], 200),
                (["available", "pending"], 200),
                (["pending", "sold"], 200)
            ]
    )
    def test_find_pet_by_status_ok(self, status, expected_result):
        response = self.petService.find_pets_by_status(status)

        data = response.json()
        if data != None:
            PetModel(**data[0])
            assert data[0]["status"] == status[0] or data[0]["status"] == status[1] 
               
        assert response.status_code == expected_result

    @pytest.mark.parametrize(
        "status, expected_result",
        (
            (["AvAiLaBlE"], 400),
            (["unknown_status"], 400),
            ([None], 400),
            ([1234], 400),
            (["available", "available"], 400),
            (["available", "sold", "available", "sold"], 400)
        )
    )
    def test_find_pet_by_status_invalid(self, status, expected_result):
        response = self.petService.find_pets_by_status(status)
        assert response.status_code == expected_result

