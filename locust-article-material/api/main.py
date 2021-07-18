import time
import uvicorn
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI()


@app.get('/hello')
def hello():
    return 'Hello World'


username = 'username'
password = 'password'
token = 'this-is-a-secret-token'


def verify_user(login_token: str = Header(...)):
    if login_token != token:
        raise HTTPException(status_code=401, detail='Who are you?')


class LoginData(BaseModel):
    username: str
    password: str


@app.post('/login')
def login(request: LoginData):
    if request.username == username and request.password == password:
        return {'success': True, 'token': token}
    return {'success': False, 'token': ''}


@app.get('/logout')
def logout():
    return {'success': True, 'message': 'success to logout'}


@app.get('/fast', dependencies=[Depends(verify_user)])
def fast():
    time.sleep(0.5)
    return 'This is such a fast endpoint'


@app.get('/slow', dependencies=[Depends(verify_user)])
def slow():
    time.sleep(3)
    return 'This is such a slow endpoint'


@app.get('/double-me/{num}', dependencies=[Depends(verify_user)])
def double_me(num: int):
    doubled = num * 2
    return {'request': num, 'response': doubled}


class SquareMeData(BaseModel):
    num: int
    nums: List[int] = [0, 1, 2]


@app.post('/square-me', dependencies=[Depends(verify_user)])
def square_me(request: SquareMeData):
    num_squared = request.num ** 2
    nums_squared = [n ** 2 for n in request.nums]
    response = SquareMeData(num=num_squared, nums=nums_squared)
    return {'request': request.json(), 'response': response.json()}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)