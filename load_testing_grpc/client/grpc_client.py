import grpc

import todo_pb2 as pb2
import todo_pb2_grpc as pb2_grpc


class TodoClient:
    def __init__(self):
        self.host = "localhost"
        self.port = 3000
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.stub = pb2_grpc.TodoServiceStub(self.channel)

    def create(self, title: str, description: str, is_completed: bool):
        request = pb2.Todo(
            id="0", title=title, description=description, is_completed=is_completed
        )
        return self.stub.Create(request)

    def update(self, todoId: str, title: str, description: str, is_completed: bool):
        request = pb2.Todo(
            id=todoId, title=title, description=description, is_completed=is_completed
        )
        return self.stub.Update(request)

    def delete(self, todoId: str):
        request = pb2.TodoId(id=todoId)
        return self.stub.Delete(request)

    def get_all(self):
        request = pb2.Empty()
        return self.stub.GetAll(request)

    def get_by_id(self, todoId: str):
        request = pb2.TodoId(id=todoId)
        return self.stub.GetById(request)
