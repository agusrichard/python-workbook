from typing import Iterable
from sqlalchemy import select, update, delete

from model import Todo, Session


class TodoCore:
    @staticmethod
    def get_all():
        todos = []
        stmt = select(Todo)
        with Session() as session:
            todos: Iterable[Todo] = session.execute(stmt).scalars().all()
            todos = [todo.to_dict() for todo in todos]

        return todos

    @staticmethod
    def get_by_id(todoId: int):
        with Session() as session:
            todo: Todo = session.query(Todo).filter(Todo.id == todoId).first()

        return todo.to_dict()

    @staticmethod
    def create(title: str, description: str, is_completed: bool):
        result = {}
        with Session() as session:
            todo: Todo = Todo(
                title=title, description=description, is_completed=is_completed
            )
            session.add(todo)
            session.commit()

            result = todo.to_dict()

        return result

    @staticmethod
    def update(todoId: int, title: str, description: str, is_completed: bool):
        result = {}
        stmt = (
            update(Todo)
            .where(Todo.id == todoId)
            .values(
                title=title,
                description=description,
                is_completed=is_completed,
            )
        )
        with Session() as session:
            session.execute(stmt)
            session.commit()

            todo: Todo = session.query(Todo).filter(Todo.id == todoId).first()
            result = todo.to_dict()

        return result

    @staticmethod
    def delete(todoId: int):
        stmt = delete(Todo).where(Todo.id == todoId)
        with Session() as session:
            session.execute(stmt)
            session.commit()
