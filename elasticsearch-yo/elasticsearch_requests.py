import requests


def get_indices():
    response = requests.get('http://es01:9200/_cat/indices?format=json')
    return response.json()


def get_shards():
    response = requests.get('http://es01:9200/_cat/shards?format=json')
    return response.json()


def create_document(data):
    request_body = data.json()
    print('request json', request_body)
    response = requests.post(
        'http://es01:9200/learn-elasticsearch/_doc', data=request_body, headers={'Content-Type': 'application/json'})
    return response.json()
