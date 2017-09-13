from flask import Flask
from workshop.database import db


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

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
