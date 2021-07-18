import time
import uvicorn
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/hello')
def hello():
    return 'Hello World'

@app.get('/fast')
def fast():
    time.sleep(0.5)
    return 'This is such a fast endpoint'

@app.get('/slow')
def slow():
    time.sleep(3)
    return 'This is such a slow endpoint'

@app.get('/double-me/{num}')
def double_me(num: int):
    doubled = num * 2
    return {'request': num, 'response': doubled}

class SquareMeData(BaseModel):
    num: int
    nums: List[int] = [0, 1, 2]

@app.post('/square-me')
def square_me(request: SquareMeData):
    num_squared = request.num ** 2
    nums_squared = [n ** 2 for n in request.nums]
    response = SquareMeData(num=num_squared, nums=nums_squared)
    return {'request': request.json(), 'response': response.json()}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)