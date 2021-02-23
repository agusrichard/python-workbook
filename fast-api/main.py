from typing import Optional, Set, List
from pydantic import BaseModel, Field, HttpUrl
from fastapi import FastAPI, Query, Path, Body
from datetime import datetime, time, timedelta
from uuid import UUID

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    id: int
    name: str = Field(..., title='Item Name', example='Ice Cream')
    price: float
    description: Optional[str] = Field('sekar', title='Item description', min_length=5, example='This thing is delicious')
    tags: Set[str] = set()
    image: Optional[Image] = None

class User(BaseModel):
    id: int
    email: str
    username: Optional[str] = ''
    fullname: Optional[str] = ''

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'email': 'sekardayu@example.com',
                'username': 'sekardayu',
                'fullname': 'Sekardayu Hana Pradiani'
            }
        }

@app.put('/item1s/{item_id}')
async def update_item1(
    *,
    item_id: int = Path(..., title='Item ID'),
    item: Item
):
    return {
        'item_id': item_id,
        'item': item
    }

@app.put('/items2/{item_id}')
async def update_item2(
    *,
    item_id: int = Path(..., title='Item ID'),
    item: Item
):
    return {
        'item_id': item_id,
        'item': item
    }

@app.post('/images/multiple')
async def save_multiple_images(images: List[Image]):
    return {
        'images': images
    }

@app.post('/user/sekar')
async def get_user(user: User):
    return {
        'user': user
    }

@app.put('/items3/{item_id}')
async def update_item3(
    item_id: UUID,
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None)
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }