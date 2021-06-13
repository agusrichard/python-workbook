from locust import HttpUser, between

from locust_tasks.light import LightTask
from locust_tasks.medium import MediumTask


class RunLoadTest(HttpUser):
    wait_time = between(1, 2)
    tasks = [LightTask, MediumTask]
