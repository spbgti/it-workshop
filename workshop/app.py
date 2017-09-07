from flask import Flask
from workshop.database import db


def create_app(mode: str) -> Flask:
    app = Flask(__name__)

    if mode is 'dev':
        from workshop.config import DevConfig
        app.config.from_object(DevConfig)
    elif mode is 'test':
        from workshop.config import TestConfig
        app.config.from_object(TestConfig)
    else:
        from workshop.config import BaseConfig
        app.config.from_object(BaseConfig)

    print('Applied config:')
    print(app.config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
