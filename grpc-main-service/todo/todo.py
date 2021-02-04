from flask import Blueprint, g
from middleware.middleware import token_required

todo_blueprint = Blueprint('todo_blueprint', __name__)


@todo_blueprint.route('/')
@token_required
def index():
    print("user data", g.user_data)
    return 'This is todo route'