import os

from flask import Flask
from flask_cors import CORS
from werkzeug.utils import find_modules, import_string


def create_app(config=None):
    app = Flask(__name__)

    app.config.update(
        DEBUG=os.environ.get('DEBUG', True)
        # more flask config settings can be defined here ideally
        # consumed from environment variables
    )

    app.config.update(config or {})

    # https://flask.palletsprojects.com/en/1.1.x/blueprints/
    # register views
    register_blueprints(app)

    # run logic when tearing down app
    # register_teardowns(app)

    return app


def register_blueprints(app):
    """Register all blueprint modules

    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('src.views'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


# def register_teardowns(app):
#     @app.teardown_appcontext
#     # uncomment and add teardown code like db disconnect here
