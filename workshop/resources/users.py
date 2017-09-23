from flask import request, current_app
from flask_restful import Resource, abort

from workshop.database import db
from workshop.models.user import User


class UsersListApi(Resource):
    """
    API Resource class for User entity
    """
    def get(self):
        query = User.query.all()
        return {
                'status': 'OK',
                'users': [i.serialized for i in query]
        }
    
    def post(self):
        login = request.json['login'] or None
        email = request.json['email'] or None
        role = request.json['role'] or 1            # Defaults to trainee role
        current_app.logger.debug(
            f"Got POST request on /users with parameters:\n"
            f"   login={login}, email={email}, role={role}"
        )
        
        if login is None or email is None:
            abort(400)          # TODO: Give proper description of what has gone wrong
            
        new_item = User(login=login, email=email, role=role)
        db.session.add(new_item)
        db.session.commit()
        
        if new_item.id is not None:
            current_app.logger.debug(
                f"Created User id {new_item.id}"
            )
            return {
                    'status': 'OK',
                    'user': new_item.serialized
            }, 201
        else:
            abort(500)          # Something really fucked up
