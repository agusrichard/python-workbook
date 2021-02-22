from fastapi import FastAPI
from enum import Enum

class Crushes(str, Enum):
    sekar = 'sekar'
    saskia = 'saskia'
    arifa = 'arifa'


app = FastAPI()

@app.get('/crushes/{crush_name}')
async def get_crush(crush_name: Crushes):
    if crush_name == Crushes.sekar:
        return {'crush': 'Sekardayu Hana Pradiani', 'message': 'She\'ll getting married soon'}
    
    if crush_name == Crushes.saskia:
        return {'crush': 'Saskia Nurul Azhima', 'message': 'Why she chose someone uglier than me? Weird shit'}
    
    return {'crush': 'Arifa Rachma', 'message': 'I dont\'t know her, but she is pretty!'}

@app.get('/files/{file_path:path}')
async def get_file(file_path: str):
    return {'message': file_path}