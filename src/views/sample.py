# sample.py

"""
    A sample view that defines the /ip endpoint.
"""

from flask import Blueprint, current_app, jsonify, request

from src.helpers.sample_helper import SampleHelper

bp = Blueprint('sample', __name__)


@bp.route('/ip', methods=['GET'])
def ip():
    response = jsonify({'my_ip': SampleHelper.get_ip_address()})
    response.status_code = 200
    return response
