from typing import List
from pydantic import BaseModel


class Address(BaseModel):
    country: str
    city: str


class CreateDocumentRequest(BaseModel):
    name: str
    age: int
    address: Address
    hobbies: List[str]
