from fastapi import FastAPI, status, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import EmailStr
from typing import List

app = FastAPI()

@app.get('/items', status_code=status.HTTP_200_OK)
async def get_item(item_name: str):
    return {'item_name': item_name}

@app.post('/users')
async def create_user(email: EmailStr = Form(...), password: str = Form(...)):
    return {
        'email': email,
        'password': password
    }

@app.post('/files')
async def create_file(file: bytes = File(...)):
    return {
        'filesize': len(file)
    }

# Upload single file
@app.post('/uploadfile')
async def create_upload_file(file: UploadFile = File(...)):
    readed = await file.read()
    print(type(readed))
    return {
        'filename': file.filename
    }

# Upload multiple data
@app.post('/multiplefiles')
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    return {'filenames': [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
    <body>
        <form action="/multiplefiles" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
    </body>
    """
    return HTMLResponse(content=content)


# Using form and file together
@app.post('/form-files')
async def create_form_files(username: str = Form(...), files: List[UploadFile] = File(...)):
    return {
        'username': username,
        'files': [file.content_type for file in files]
    }