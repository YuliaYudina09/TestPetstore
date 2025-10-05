from pydantic import BaseModel, StrictInt

class CategoryModel(BaseModel):
    id: StrictInt
    name: str