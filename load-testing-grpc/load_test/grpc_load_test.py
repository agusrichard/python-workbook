import grpc
import todo_pb2 as pb2
import todo_pb2_grpc as pb2_grpc
from locust import HttpUser, User, task, between
from locust.exception import LocustError
from locust.user.task import LOCUST_STATE_STOPPING
import time
import grpc.experimental.gevent as grpc_gevent

grpc_gevent.init_gevent()


class GrpcClient:
    def __init__(self, environment, stub):
        self.env = environment
        self._stub_class = stub.__class__
        self._stub = stub

    def __getattr__(self, name):
        func = self._stub_class.__getattribute__(self._stub, name)

        def wrapper(*args, **kwargs):
            request_meta = {
                "request_type": "grpc",
                "name": name,
                "start_time": time.time(),
                "response_length": 0,
                "exception": None,
                "context": None,
                "response": None,
            }
            start_perf_counter = time.perf_counter()
            try:
                request_meta["response"] = func(*args, **kwargs)
                print("reqquest_meta", request_meta["response"])
                # request_meta["response_length"] = len(request_meta["response"].message)
            except grpc.RpcError as e:
                request_meta["exception"] = e
            request_meta["response_time"] = (
                time.perf_counter() - start_perf_counter
            ) * 1000
            self.env.events.request.fire(**request_meta)
            return request_meta["response"]

        return wrapper


class GrpcUser(User):
    abstract = True

    stub_class = None

    def __init__(self, environment):
        super().__init__(environment)
        for attr_value, attr_name in (
            (self.host, "host"),
            (self.stub_class, "stub_class"),
        ):
            if attr_value is None:
                raise LocustError(f"You must specify the {attr_name}.")
        self._channel = grpc.insecure_channel(self.host)
        self._channel_closed = False
        stub = self.stub_class(self._channel)
        self.client = GrpcClient(environment, stub)


class TodoGrpcUser(GrpcUser):
    host = "localhost:3000"
    stub_class = pb2_grpc.TodoServiceStub

    @task
    def get_all(self):
        if not self._channel_closed:
            request = pb2.Empty()
            self.client.GetAll(request)
        time.sleep(1)

    @task
    def create(self):
        if not self._channel_closed:
            request = pb2.Todo(
                id="0", title="test", description="test", is_completed=False
            )
            self.client.Create(request)
        time.sleep(1)
