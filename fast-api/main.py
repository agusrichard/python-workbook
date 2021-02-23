from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom exception
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

# The handler for our custom exception
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={'message': f'Oops! {exc.name} did something. There goes a rainbow...'}
    )


@app.get('/items/{item_id}')
async def get_item(item_id: int):
    lists = [i for i in range(10)]
    print(lists)

    if item_id == 0:
        raise UnicornException(f'{item_id}')

    if item_id not in lists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item is not found', headers={'X-Error': 'There goes my error'})
    return {'item': lists[item_id]}