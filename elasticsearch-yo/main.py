import uvicorn
from fastapi import FastAPI

import schemas
import elasticsearch_requests

app = FastAPI(title='ElasticSearch Yo')


@app.get('/')
def root():
    return 'Sekardayu Hana Pradiani'


@app.get('/indices')
def get_indices():
    result = elasticsearch_requests.get_indices()
    return result


@app.get('/shards')
def get_shards():
    result = elasticsearch_requests.get_shards()
    return result


@app.post('/create-document')
def create_document(request: schemas.CreateDocumentRequest):
    result = elasticsearch_requests.create_document(request)
    return result


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
