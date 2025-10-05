from pydantic import BaseModel, StrictInt
from typing import List
from services.pet_service.models import category_model, tags_model

class PetModel(BaseModel):
    id: StrictInt
    category: category_model.CategoryModel
    name: str
    photoUrls: List[str]
    tags: List[tags_model.TagsModel] | None
    status: str