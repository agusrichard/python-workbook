from flask import Blueprint
from .client import AuthClient

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/')
def index():
    auth_client = AuthClient()
    result = auth_client.register(username='agusrichard',
                                  password='agusrichard')
    return f'Response from server auth {result}'