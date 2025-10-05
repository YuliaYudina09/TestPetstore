from base.links import Links
from services.pet_service.endpoints import Endpoints
from services.pet_service.payloads import Payloads
import requests

class PetService:

    def __init__(self):
        self.links = Links()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    def upload_an_image(self, id, file_path):
        data = {
            "additionalMetadata": "additionalMetadata"
        }

        file = {
            "file": open(file_path, "rb")
        }

        return requests.post(f"{self.links.BASE_URL}{self.endpoints.upload_an_image(id)}", data = data, files = file)
    
    def add_a_new_pet(self, payload=None):
        if payload == None: payload = self.payloads.add_a_new_pet
        return requests.post(f"{self.links.BASE_URL}{self.endpoints.add_a_new_pet}", json = payload)
    
    def update_a_pet(self, payload=None):
        if payload == None: payload = self.payloads.update_a_pet
        return requests.put(f"{self.links.BASE_URL}{self.endpoints.update_a_pet}", json = payload)
    
    def find_pets_by_status(self, status):
        params = {
            "status": status
        }
        return requests.get(f"{self.links.BASE_URL}{self.endpoints.find_pets_by_status}", params = params)
    
    def find_pet_by_id(self, id):
        return requests.get(f"{self.links.BASE_URL}{self.endpoints.find_pet_by_id(id)}")
    
    def update_a_pet_with_form_data(self, id, name, status):
        data = {
            "name": name,
            "status": status
        }
        return requests.post(f"{self.links.BASE_URL}{self.endpoints.update_a_pet_with_form_data(id)}", data=data)
    
    def delete_a_pet(self, id):
        api_key = {"accept": "application/json"}
        return requests.delete(f"{self.links.BASE_URL}{self.endpoints.delete_a_pet(id)}", headers=api_key)
