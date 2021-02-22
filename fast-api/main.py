from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get('/items1/{item_id}')
async def get_item1(
    item_id: int = Path(..., title='Item ID', description='You better provide the item ID'),
    query: Optional[str] = Query(None, title='Query')
):
    return {
        'item_id': item_id,
        'query': query
    }

@app.get('/items2/{item_id}')
async def get_item2(
    query:str,
    item_id:int = Path(..., title='Item ID')
):
    return {
        'item_id': item_id,
        'query': query
    }

@app.get('/items3/{item_id}')
async def get_item3(
    *, item_id:int = Path(..., title='Item ID'),
    query:str
):
    return {
        'item_id': item_id,
        'query': query
    }

# Number validations
@app.get('/items4/{item_id}')
async def get_item4(
    *, item_id:int = Path(..., title='Item ID', ge=5),
    query:str
):
    return {
        'item_id': item_id,
        'query': query
    }

