from flask import Flask, jsonify, request

from core import TodoCore

app = Flask(__name__)


@app.get("/")
def index():
    return "Hello World!"


@app.get("/get-all")
def get_all():
    result = TodoCore.get_all()
    return jsonify(result)


@app.get("/get-by-id/<todoId>")
def get_by_id(todoId: str):
    result = TodoCore.get_by_id(todoId)
    return jsonify(result)


@app.post("/create")
def create():
    title = request.form["title"]
    description = request.form["description"]
    is_completed = request.form["is_completed"] == "true"
    result = TodoCore.create(title, description, is_completed)
    return jsonify(result)


@app.put("/update/<todoId>")
def update(todoId: str):
    title = request.form["title"]
    description = request.form["description"]
    is_completed = request.form["is_completed"] == "true"
    result = TodoCore.update(todoId, title, description, is_completed)
    return jsonify(result)


@app.delete("/delete/<todoId>")
def delete(todoId: str):
    TodoCore.delete(todoId)
    return "Deleted"


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
