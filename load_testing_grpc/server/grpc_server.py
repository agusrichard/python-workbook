import grpc
from concurrent import futures
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, update, delete

from model import Base, Todo

engine = create_engine("sqlite:///dev.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

import todo_pb2 as pb2
import todo_pb2_grpc as pb2_grpc


class TodoService(pb2_grpc.TodoServiceServicer):
    def GetAll(self, request, context):
        todos = []
        stmt = select(Todo)
        with Session() as session:
            todos = session.execute(stmt).scalars().all()
            todos = [
                {
                    "id": str(todo.id),
                    "title": todo.title,
                    "description": todo.description,
                    "is_completed": todo.is_completed,
                }
                for todo in todos
            ]
        return pb2.TodoList(todos=todos)

    def GetById(self, request, context):
        with Session() as session:
            todo = session.query(Todo).filter(Todo.id == request.id).first()
            result = {
                "id": str(todo.id),
                "title": todo.title,
                "description": todo.description,
                "is_completed": todo.is_completed,
            }
        return pb2.Todo(**result)

    def Create(self, request, context):
        result = {}
        title = request.title
        description = request.description
        is_completed = request.is_completed

        with Session() as session:
            todo = Todo(title=title, description=description, is_completed=is_completed)
            session.add(todo)
            session.commit()
            result = {
                "id": str(todo.id),
                "title": todo.title,
                "description": todo.description,
                "is_completed": todo.is_completed,
            }

        return pb2.Todo(**result)

    def Update(self, request, context):
        stmt = (
            update(Todo)
            .where(Todo.id == request.id)
            .values(
                title=request.title,
                description=request.description,
                is_completed=request.is_completed,
            )
        )
        with Session() as session:
            session.execute(stmt)
            session.commit()

            todo = session.query(Todo).filter(Todo.id == request.id).first()
            result = {
                "id": str(todo.id),
                "title": todo.title,
                "description": todo.description,
                "is_completed": todo.is_completed,
            }

        return pb2.Todo(**result)

    def Delete(self, request, context):
        stmt = delete(Todo).where(Todo.id == request.id)
        with Session() as session:
            session.execute(stmt)
            session.commit()
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
