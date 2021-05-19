import uvicorn
from fastapi import FastAPI

app = FastAPI(title='ElasticSearch Yo')


@app.get('/')
def root():
    return 'Sekardayu Hana Pradiani'


if __name__ == '__main__':
    uvicorn.run(app, debug=True)
