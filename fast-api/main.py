from typing import Optional
from fastapi import FastAPI, Depends, Header, HTTPException, status, Body
from pydantic import BaseModel


app = FastAPI()

async def common_parameters(query: Optional[str] = None, skip: int = 0, limit: int = 10):
    return {'query': query, 'skip': skip, 'limit': limit}

class CommonQueryParams:
    def __init__(self, query: Optional[str] = None, skip: int = 0, limit: int = 10):
        self.query = query
        self.skip = skip
        self.limit = limit

    def get_query(self):
        return self.query


@app.get('/items')
async def get_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get('/users')
async def get_users(commons: CommonQueryParams = Depends(CommonQueryParams)):
    print(commons.get_query())
    return commons

@app.get('/menus')
async def get_menus(commons: CommonQueryParams = Depends()):
    return commons


# =================================================================
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = ''


async def body_extractor(body_item: Item):
    return {'item': body_item}

async def body_query_extractor(item: dict = Depends(body_extractor), query: Optional[str] = None):
    return {
        'item': item,
        'query': query
    }

@app.post('/items')
async def create_item(inpt: dict = Depends(body_query_extractor)):
    return inpt

# =================================================================
async def verify_token(token: str = Header(...)):
    if token != 'sekar':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not allowed, because you are not Sekar. I dont love you!')

@app.post('/users', dependencies=[Depends(verify_token)])
async def create_user(email: str = Body(..., embed=True)):
    return {
        'email': email
    }