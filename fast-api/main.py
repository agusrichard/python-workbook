from fastapi import FastAPI

app = FastAPI()

fake_db = [{'id': num, 'message': f'message {num}'} for num in range(10)]

# Using query parameters
@app.get('/items1')
async def get_items1(skip: int = 0, limit: int = 10):
    print('take', limit)
    return fake_db[skip:limit+skip]

# Using query paramaeters and path parameters
@app.get('/items/{user_id}/{item_id}')
async def get_items2(user_id: int, item_id: int, skip: int = 0, limit: int = 10):
    return {
        'user_id': user_id,
        'item_id': item_id,
        'skip': skip,
        'limit': limit
    }