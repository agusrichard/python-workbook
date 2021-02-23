from typing import Optional, List
from fastapi import FastAPI, Cookie, Header

app = FastAPI()

@app.get('/items/')
async def get_items(ads_id: Optional[str] = Cookie(None)):
    print('ads_id', ads_id)
    return {
        'ads_id': ads_id
    }

@app.get('/users')
async def get_users(token_auth: str = Header(''), x_token: Optional[List[str]] = Header(None)):
    return {
        'token-auth': token_auth,
        'x-token-values': x_token
    }