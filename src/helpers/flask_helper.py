# flask_helper.py

"""
    Helper for re-usable Flask related logic.  Ideally it is the only helper
    that should import current_app from Flask to allow all other helper classes
    to be re-used outside off the Flask context (like w/ doit).
"""

from flask import current_app

from src.helpers.base_helper import BaseHelper


class FlaskHelper(BaseHelper):

    def __init__(self):
        pass
