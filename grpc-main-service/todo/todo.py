import json
from flask import Blueprint, g, jsonify, request

from todo.client import TodoClient
from middleware.middleware import token_required

todo_blueprint = Blueprint('todo_blueprint', __name__)


@todo_blueprint.route('/create', methods=['POST'])
@token_required
def create_todo():
    try:
        user_data = g.user_data
        title = request.json.get('title')
        description = request.json.get('description')
        client = TodoClient()
        client.create_todo(title=title,
                           description=description,
                           user_id=user_data.get('ID'))
        return jsonify({'success': True, 'message': 'Success to create todo'})
    except:
        return jsonify({
            'success': False,
            'message': 'Please provide the required fields'
        })


@todo_blueprint.route('/get', methods=['GET'])
@token_required
def get_todos():
    try:
        user_data = g.user_data
        client = TodoClient()
        result = client.get_todos(user_id=user_data.get('ID'))
        return jsonify({
            'success': True,
            'message': 'Success to get todos',
            'data': json.loads(result.data)
        })
    except:
        return jsonify({
            'success': False,
            'message': 'Please provide the required fields',
            'data': []
        })
