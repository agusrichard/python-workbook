from typing import Optional, List
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI
from uuid import UUID, uuid4

# app instantiation
app = FastAPI()

# User models definitions
class UserBase(BaseModel):
    email: str
    username: Optional[str] = ''
    fullname: Optional[str] = ''

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    id: UUID

class UserInDB(UserOut):
    hashed_password: str


@app.post('/users1')
async def create_user1(user_in: UserIn):
    return user_in

@app.post('/users2', response_model=UserOut)
async def create_user2(user: UserIn):
    user_dict = user.dict()
    user_dict.update({'id': uuid4()})
    return user_dict

# Extra Models --- It's better to have several models to define request and response
def fake_password_hasher(password):
    return 'sekardayu' + password

def fake_save_user(userin: UserIn):
    hashed_password = fake_password_hasher(userin.password)
    user = UserInDB(**userin.dict(), hashed_password=hashed_password, id=uuid4())
    print('User saved! Not really')
    return user

@app.post('/users3', response_model=UserOut)
async def create_user3(user: UserIn):
    user = fake_save_user(user)
    return user


# For item
class Item(BaseModel):
    name: str
    description: Optional[str] = ''
    price: float
    tax: float = 0.1
    tags: List[str] = []


@app.post('/items', response_model=Item, response_model_exclude_unset=True)
async def create_item(item: Item):
    return item