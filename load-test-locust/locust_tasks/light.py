import random
from datetime import datetime, timezone
from locust import task, between, TaskSet

strings_choices = ['alpha', 'beta', 'gamma']


class LightTask(TaskSet):
    wait_time = between(1, 2)

    @task(1)
    def lightv1_create(self):
        request = {
            'action': 'CREATE',
            'data': self.generate_light_create_request()
        }
        self.client.post('/v1/light/create', json=request)

    @task(3)
    def lightv1_get(self):
        request = {
            'action': 'GET',
            'query': self.generate_light_get_request()
        }
        self.client.post('/v1/light/get', json=request)

    @task(1)
    def lightv2_create(self):
        request = {
            'action': 'CREATE',
            'data': self.generate_light_create_request()
        }
        self.client.post('/v2/light/create', json=request)

    @task(3)
    def lightv2_get(self):
        request = {
            'action': 'GET',
            'query': self.generate_light_get_request()
        }
        self.client.post('/v2/light/get', json=request)

    @staticmethod
    def generate_light_create_request():
        choices = [0, 1, 2]
        if random.choice(choices) == 0:
            request = {
                'fieldOne': random.choice(strings_choices),
                'fieldTwo': random.uniform(0, 10),
                'fieldThree': random.choice(strings_choices),
                'fieldFour': datetime.now(timezone.utc).astimezone().isoformat()
            }
        elif random.choice(choices) == 1:
            request = {
                'fieldOne': random.choice(strings_choices),
                'fieldTwo': random.uniform(0, 10),
                'fieldFour': datetime.now(timezone.utc).astimezone().isoformat()
            }
        else:
            request = {
                'fieldOne': random.choice(strings_choices),
                'fieldTwo': random.uniform(0, 10),
                'fieldThree': random.choice(strings_choices),
            }
        return request

    @staticmethod
    def generate_light_get_request():
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
