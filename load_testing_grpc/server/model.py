from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    is_completed = Column(Boolean)

    def __repr__(self) -> str:
        return f"<Todo(id={self.id}, title='{self.title}', description='{self.description}')>"
