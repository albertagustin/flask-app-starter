import os

from flask import Flask
from werkzeug.utils import find_modules, import_string


def create_app(config=None):
    app = Flask(__name__)

    # define app configuration settings as env variables
    app.config.update(
        DEBUG=os.environ.get('DEBUG', True)
    )

    app.config.update(config or {})

    register_blueprints(app)
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
#     def close_db(error):
#         BaseAzureDocDB().close_db()
