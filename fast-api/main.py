from typing import Optional
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: int
    description: str = ''

class User(BaseModel):
    id: int
    email: str
    username: Optional[str] = ''
    fullname: Optional[str] = ''



@app.put('/items1/{item_id}')
async def update_item1(
    *,
    item_id:int = Path(..., title='Item ID', description='You have to provide item id to access it'),
    query: Optional[str] = None,
    body: Optional[Item] = None
):
    result = {'item_id': item_id}
    if query:
        result.update({'query': query})
    if body:
        result.update({'body': body})

    return result

@app.put('/items2/{item_id}')
async def update_item2(
    *,
    item_id: int,
    item: Item,
    user: Optional[User] = None
):
    result = {
        'item_id': item_id,
        'item': item
    }

    if user:
        result.update({'user': user})

    return result

@app.put('/items3/{item_id}')
async def update_item3(
    *,
    item_id: int,
    item: Item,
    user: Optional[User] = None,
    importance: str = Body(...)
):
    result = {
        'item_id': item_id,
        'item': item,
        'importance': importance
    }

    if user:
        result.update({'user': user})

    return result

# Ember the single body parameter
@app.put('/items4/{item_id}')
async def update_item4(
    *,
    item_id: int,
    item: Item = Body(..., embed=True)
):
    return {
        'item_id': item_id,
        'item': item
    }
