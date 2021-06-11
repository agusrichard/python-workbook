from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def light(self):
        self.client.get('/light')

    @task
    def medium(self):
        self.client.get('/medium')

    @task
    def heavy(self):
        self.client.get('/heavy')
