class Endpoints:
    
    upload_an_image = lambda self, id: f"/pet/{id}/uploadImage"
    add_a_new_pet = "/pet"
    update_a_pet = "/pet"
    find_pets_by_status = "/pet/findByStatus"
    find_pet_by_id = lambda self, id: f"/pet/{id}"
    update_a_pet_with_form_data = lambda self, id: f"/pet/{id}"
    delete_a_pet = lambda self, id: f"/pet/{id}"
