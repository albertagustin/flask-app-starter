import pytest

from flask import Flask, jsonify
from src import create_app


@pytest.fixture
def app():
    app = create_app()
    app.debug = True

    import src.views
    return app
