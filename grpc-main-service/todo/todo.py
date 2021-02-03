from flask import Blueprint

todo_blueprint = Blueprint('todo_blueprint', __name__)


@todo_blueprint.route('/')
def index():
    return 'This is todo route'