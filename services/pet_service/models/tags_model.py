from pydantic import BaseModel, StrictInt

class TagsModel(BaseModel):
    id: StrictInt
    name: str