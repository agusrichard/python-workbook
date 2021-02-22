from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict

class User(BaseModel):
    id: int
    email: str
    username: Optional[str] = None
    fullname: Optional[str] = None
    age: Optional[int] = None


app = FastAPI()

@app.post('/user')
async def post_user(user: User):
    return {'user': user}

@app.post('/item/{item_id}')
async def post_item(user: User, item_id: int):
    return {
        'user': user,
        'item': item_id
    }

@app.get('/q')
async def get_q(q: Optional[bool] = None):
    if q:
        return {'data': 'Sekardayu Hana Pradiani'}
    return {'data': 'Saskia Nurul Azhima'}