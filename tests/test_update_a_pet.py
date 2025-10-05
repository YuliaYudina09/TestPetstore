from base.base_test import BaseTest
from services.pet_service.models.model import PetModel
import pytest

class TestUpdatePet(BaseTest):

    def test_update_a_pet_ok(self):
        response = self.petService.update_a_pet()

        data = response.json()

        payload = self.petService.payloads.update_a_pet

        PetModel(**data)

        assert data["id"] == payload["id"]
        assert data["category"]["id"] == payload["category"]["id"]
        assert data["category"]["name"] == payload["category"]["name"]
        assert data["name"] == payload["name"]
        assert data["photoUrls"] == payload["photoUrls"]
        assert data["tags"][0]["id"] == payload["tags"][0]["id"]
        assert data["tags"][0]["name"] == payload["tags"][0]["name"]
        assert data["status"] == payload["status"]

        assert response.status_code == 200

    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (None, 1, "Cats", "Max", "http://max.png", 5, "Funny", "available", 200),
                (1, None, "Cats", "Max", "http://max.png", 5, "Funny", "available", 200),
                (1, 1, None, "Max", "http://max.png", 5, "Funny", "available", 200),
                (1, 1, "Cats", "Max", "http://max.png", None, "Funny", "available", 200),
                (1, 1, "Cats", "Max", "http://max.png", 5, None, "available", 200),
                (1, 1, "Cats", "Max", "http://max.png", 5, "Funny", None, 200)
            }
    )
    def test_update_a_pet_with_empty_optional_values_ok(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result

    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (0, 1, "Cats", "Max", "http://max.png", 5, "Funny", "available", 400),
                (-1, 1, "Cats", "Max", "http://max.png", 5, "Funny", "available", 400),
                (2.3, 1, "Cats", "Max", "http://max.png", 5, "Funny", "available", 400),
                ("1", 1, "Cats", "Max", "http://max.png", 5, "Funny", "available", 400),
            }
    )
    def test_update_a_pet_invalid_id(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result

    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (1, 0, "Cats", "Max", "http://max.png", 5, "Funny", "available", 400),
                (1, -1, "Cats", "Max", "http://max.png", 5, "Funny", "available", 400),
                (1, 2.3, "Cats", "Max", "http://max.png", 5, "Funny", "available", 400),
                (1, "1", "Cats", "Max", "http://max.png", 5, "Funny", "available", 400),
            }
    )
    def test_update_a_pet_invalid_category_id(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result

    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (1, 1, "Cats", "Max", "http://max.png", 0, "Funny", "available", 400),
                (1, 1, "Cats", "Max", "http://max.png", -1, "Funny", "available", 400),
                (1, 1, "Cats", "Max", "http://max.png", 2.3, "Funny", "available", 400),
                (1, 1, "Cats", "Max", "http://max.png", "5", "Funny", "available", 400),
            }
    )
    def test_update_a_pet_invalid_tags_id(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result

    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (1, 1, 10, "Max", "http://max.png", 5, "Funny", "available", 405),
                (1, 1, 5.7, "Max", "http://max.png", 5, "Funny", "available", 405),
                (1, 1, "Abcd", "Max", "http://max.png", 5, "Funny", "available", 405)
            }
    )
    def test_update_a_pet_invalid_category_name(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result 

    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (1, 1, "Cats", 10, "http://max.png", 5, "Funny", "available", 405),
                (1, 1, "Cats", 5.8, "http://max.png", 5, "Funny", "available", 405),
                (1, 1, "Cats", None, "http://max.png", 5, "Funny", "available", 405),
                (1, 1, "Cats", "", "http://max.png", 5, "Funny", "available", 405)
            }
    )
    def test_update_a_pet_invalid_name(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result 

    @pytest.mark.parametrize(
            "photoUrls, expected_result",
            {
                ("", 405),
                (123, 405),
                (None, 405)
            })
    def test_update_a_pet_invalid_photoUrls(self, photoUrls, expected_result):
        payload = {
            "id": 1,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [photoUrls],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
            }
        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result
    
    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (1, 1, "Cats", "Max", "http://max.png", 0, "Funny", "available", 405),
                (1, 1, "Cats", "Max", "http://max.png", -1, "Funny", "available", 405),
                (1, 1, "Cats", "Max", "http://max.png", 2.3, "Funny", "available", 405),
                (1, 1, "Cats", "Max", "http://max.png", "5", "Funny", "available", 405),
            }
    )
    def test_update_a_pet_invalid_tags_id(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result

    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (1, 1, "Cats", "Max" , "http://max.png", 5, 10, "available", 405),
                (1, 1, "Cats", "Max", "http://max.png", 5, 5.8, "available", 405)
            }
    )
    def test_update_a_pet_invalid_tags_name(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result 

    @pytest.mark.parametrize(
            "id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result", 
            {
                (1, 1, "Cats", "Max" , "http://max.png", 5, "Funny", 222, 405),
                (1, 1, "Cats", "Max", "http://max.png", 5, "Funny", "abcd", 405)
            }
    )
    def test_update_a_pet_invalid_status(self, id, category_id, category_name, name, photoUrls, tags_id, tags_name, status, expected_result):
        payload = {
            "id": id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": name,
            "photoUrls": [
                photoUrls
            ],
            "tags": [
                {
                "id": tags_id,
                "name": tags_name
                }
            ],
            "status": status
        }

        response = self.petService.update_a_pet(payload)
        assert response.status_code == expected_result 
