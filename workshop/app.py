from flask import Flask
from flask_restful import Api

from workshop.database import db
from workshop.resources import ProjectsListApi, UsersListApi


def create_app(mode: str) -> Flask:
    """
    Flask application factory function
    
    Args:
        mode: application execution mode, defines config used. Choices available: ['dev', 'test'].

    Returns:
        `Flask` object.
    """
    app = Flask(__name__)
    api = Api(app)

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

    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    api.add_resource(ProjectsListApi, '/projects')
    api.add_resource(UsersListApi, '/users')

    return app
