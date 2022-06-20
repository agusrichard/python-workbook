import grpc
from concurrent import futures

from core import TodoCore

import todo_pb2 as pb2
import todo_pb2_grpc as pb2_grpc


class TodoService(pb2_grpc.TodoServiceServicer):
    def GetAll(self, request, context):
        todos = TodoCore.get_all()
        return pb2.TodoList(todos=todos)

    def GetById(self, request, context):
        result = TodoCore.get_by_id(int(request.id))
        return pb2.Todo(**result)

    def Create(self, request, context):
        result = TodoCore.create(
            title=request.title,
            description=request.description,
            is_completed=request.is_completed,
        )
        return pb2.Todo(**result)

    def Update(self, request, context):
        result = TodoCore.update(
            todoId=int(request.id),
            title=request.title,
            description=request.description,
            is_completed=request.is_completed,
        )
        return pb2.Todo(**result)

    def Delete(self, request, context):
        TodoCore.delete(int(request.id))
        return pb2.Empty()


def serve():
    print("Running on port 3000")
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), grpc_server)
    grpc_server.add_insecure_port("[::]:3000")
    grpc_server.start()
    grpc_server.wait_for_termination()


if __name__ == "__main__":
    serve()
