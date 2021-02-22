from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

# Additional validation to make sure the string is not exceeding 100 characters
@app.get('/items/{item_id}')
async def get_items(item_id: int, query: Optional[str] = Query(None, max_length=100)):
    return {
        'item_id': item_id,
        'query': query
    }

@app.get('/menus')
async def get_menus(query: Optional[str] = Query(None, min_length=5, max_length=100, regex='^sekar')):
    return {
        'query': query
    }

@app.get('/read_items')
async def read_items(query: str = Query('sekar', min_length=5, max_length=100)):
    return {
        'query': query
    }

# Let's create the same handler using query but required
@app.get('/get_items1')
async def get_items1(query: str = Query(..., min_length=5)):
    return {
        'query': query
    }

# Query parameters which appear multiple times in the URL
@app.get('/get_items2')
async def get_items2(query: Optional[List[str]] = Query(None)):
    return {
        'query': query
    }

# Let's change it so the FastAPI won't check the content type of the list
@app.get('/get_items3')
async def get_items3(query:list = Query([])):
    return {
        'query': query
    }

# Give us a better description about parameters we have to provide
@app.get('/get_items4')
async def get_items4(query:Optional[str] = Query(
    None, title='Sekardayu', description='She is getting married you know!', min_length=5
)):
    return {
        'query': query
    }

# Using an alias for query parameter
@app.get('/get_items5')
async def get_items5(query:Optional[str] = Query(None, alias='item-id')):
    return {
        'query': query
    }