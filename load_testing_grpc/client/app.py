from flask import Flask, jsonify, request
from grpc_client import TodoClient

app = Flask(__name__)
client = TodoClient()


@app.get("/")
def index():
    return "Hello World!"


@app.get("/get-all")
def get_all():
    result = client.get_all()
    result = [
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "is_completed": todo.is_completed,
        }
        for todo in result.todos
    ]
    return jsonify(result)


@app.get("/get-by-id/<todoId>")
def get_by_id(todoId: str):
    result = client.get_by_id(todoId)
    return jsonify(
        {
            "id": result.id,
            "title": result.title,
            "description": result.description,
            "is_completed": result.is_completed,
        }
    )


@app.post("/create")
def create():
    title = request.form["title"]
    description = request.form["description"]
    is_completed = request.form["is_completed"] == "true"
    result = client.create(title, description, is_completed)
    return jsonify(
        {
            "id": result.id,
            "title": result.title,
            "description": result.description,
            "is_completed": result.is_completed,
        }
    )


@app.put("/update/<todoId>")
def update(todoId: str):
    title = request.form["title"]
    description = request.form["description"]
    is_completed = request.form["is_completed"] == "true"
    result = client.update(todoId, title, description, is_completed)
    return jsonify(
        {
            "id": result.id,
            "title": result.title,
            "description": result.description,
            "is_completed": result.is_completed,
        }
    )


@app.delete("/delete/<todoId>")
def delete(todoId: str):
    client.delete(todoId)
    return "Deleted"


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
