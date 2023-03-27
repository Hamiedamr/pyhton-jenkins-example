from pydantic import BaseModel

class InputModel(BaseModel):
    name: str
    title: str
    age: int