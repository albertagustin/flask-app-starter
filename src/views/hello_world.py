from flask import Blueprint, jsonify

bp = Blueprint('helloworld', __name__)


@bp.route('/helloworld', methods=['GET'])
def hello_world():
    response = jsonify({'msg': 'Hello You!'})
    response.status_code = 200
    return response
