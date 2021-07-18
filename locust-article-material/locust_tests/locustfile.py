import time
import random
import gevent
from locust import HttpUser, task, between, TaskSet, events
from locust.runners import STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP, WorkerRunner


def fast_task(user):
    user.client.get('/fast', headers={'login-token': user.login_token})


def slow_task(user):
    user.client.get('/slow', headers={'login-token': user.login_token})


class ProcessNumberTask(TaskSet):
    @task(1)
    def square_me(self):
        random_number = random.randint(0, 10)
        random_numbers = [random.randint(0, 10) for _ in range(1000)]
        request_body = {'num': random_number, 'nums': random_numbers}
        self.client.post('/square-me', json=request_body, headers={'login-token': self.user.login_token})

    @task(3)
    def double_me(self):
        random_number = random.randint(0, 10)
        self.client.get(f'/double-me/{random_number}', name='/double-me', headers={'login-token': self.user.login_token})


class TestUser(HttpUser):
    wait_time = between(0.5, 2.5)
    tasks = [fast_task, slow_task, ProcessNumberTask]
    login_token = ''
    is_login = False

    def on_start(self):
        with self.client.post('/login', json={'username': 'username', 'password': 'password'}) as response:
            if response.status_code == 200:
                self.login_token = response.json()['token']
                self.is_login = True

    def on_stop(self):
        with self.client.get('/logout') as response:
            if response.status_code == 200:
                self.login_token = ''
                self.is_login = False

    @events.init.add_listener
    def on_locust_init(environment, **_kwargs):
        def checker(environment):
            while environment.runner.state not in [STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP]:
                time.sleep(1)
                if environment.runner.stats.total.num_requests > 5000:
                    environment.runner.quit()
                    return

        if not isinstance(environment.runner, WorkerRunner):
            gevent.spawn(checker, environment)

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        print('Starting test')

    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        print('Stopping test')

    @task
    def hello_world(self):
        self.client.get('/hello')
