import random
from datetime import datetime, timezone
from locust import task, between, TaskSet

strings_choices = ['alpha', 'beta', 'gamma']


class MediumTask(TaskSet):
    wait_time = between(1, 2)

    @task(1)
    def mediumv1_create(self):
        request = {
            'action': 'CREATE',
            'data': self.generate_medium_create_request()
        }
        self.client.post('/v1/medium/create', json=request)

    @task(3)
    def mediumv1_get(self):
        request = {
            'action': 'GET',
            'query': self.generate_medium_get_request()
        }
        self.client.post('/v1/medium/get', json=request)

    @task(1)
    def mediumv2_create(self):
        request = {
            'action': 'CREATE',
            'data': self.generate_medium_create_request()
        }
        self.client.post('/v2/medium/create', json=request)

    @task(3)
    def mediumv2_get(self):
        request = {
            'action': 'GET',
            'query': self.generate_medium_get_request()
        }
        self.client.post('/v2/medium/get', json=request)

    @staticmethod
    def generate_medium_create_request():
        request = {
            'fieldOne': random.choice(strings_choices),
            'fieldTwo': random.uniform(0, 10),
            'fieldThree': random.choice(strings_choices),
            'fieldFive': random.randint(0, 10),
            'fieldSix': random.choice(strings_choices),
            'fieldSeven': random.uniform(0, 10),
            'fieldEight': random.choice(strings_choices),
            'fieldTen': random.randint(0, 10),
            'fieldEleven': random.choice(strings_choices),
            'fieldTwelve': random.uniform(0, 10),
            'fieldThirteen': random.choice(strings_choices),
            'mediumSmallModelList': [
                {
                    'fieldOne': random.choice(strings_choices),
                    'fieldTwo': random.uniform(0, 10),
                    'fieldThree': random.choice(strings_choices),
                    'fieldFour': datetime.now(timezone.utc).astimezone().isoformat()
                },
                {
                    'fieldOne': random.choice(strings_choices),
                    'fieldTwo': random.uniform(0, 10),
                    'fieldThree': random.choice(strings_choices),
                    'fieldFour': datetime.now(timezone.utc).astimezone().isoformat()
                },
                {
                    'fieldOne': random.choice(strings_choices),
                    'fieldTwo': random.uniform(0, 10),
                    'fieldThree': random.choice(strings_choices),
                    'fieldFour': datetime.now(timezone.utc).astimezone().isoformat()
                }
            ]
        }

        return request

    @staticmethod
    def generate_medium_get_request():
        choices = [20, 50, 100]
        request = {
            'skip': random.choice(choices),
            'take': random.choice(choices),
            'filters': [
                {
                    'type': 'text',
                    'field': 'field_one',
                    'value': random.choice(strings_choices)
                }
            ]
        }

        return request
