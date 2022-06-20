from locust import HttpUser, User, task, between


class TodoRestUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(0.5, 2.5)

    @task
    def get_all(self):
        self.client.get("/get-all")

    @task
    def create(self):
        self.client.post(
            "/create", {"title": "test", "description": "test", "is_completed": False}
        )
