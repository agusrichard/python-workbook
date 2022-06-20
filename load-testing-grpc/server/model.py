from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean

Base = declarative_base()

engine = create_engine("sqlite:///dev.db")
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    is_completed = Column(Boolean)

    def __repr__(self) -> str:
        return f"<Todo(id={self.id}, title='{self.title}', description='{self.description}')>"

    def to_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed,
        }
