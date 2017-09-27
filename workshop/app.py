from flask import Flask
from flask_restful import Api as API

from workshop.database import db
from workshop.resources import ProjectsListAPI, UsersListAPI


def create_app(mode: str) -> Flask:
    """
    Flask application factory function
    
    Args:
        mode: application execution mode, defines config used. Choices available: ['dev', 'test'].

    Returns:
        `Flask` object.
    """
    app = Flask(__name__)

    if mode == 'dev':
        from workshop.config import DevConfig
        app.config.from_object(DevConfig)
    elif mode == 'test':
        from workshop.config import TestConfig
        app.config.from_object(TestConfig)
    else:
        from workshop.config import BaseConfig
        app.config.from_object(BaseConfig)

    app.logger.debug(f"Applied config: {app.config}")

    api = register_api(app)
    register_resources(api)

    return app


def register_api(app: Flask) -> API:
    """
    Register Flask extensions
    Args:
        app: The application object to extend

    Returns:
        `API` object
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = API(app)
    return api


def register_resources(app: API):
    """
    Register API resources
    Args:
        app: The application object to use
    """
    app.add_resource(ProjectsListAPI, '/projects')
    app.add_resource(UsersListAPI, '/users')
