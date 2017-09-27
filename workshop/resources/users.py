from flask import request, current_app
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError

from workshop.database import db
from workshop.models.user import User


class UsersListAPI(Resource):
    """
    API Resource class for User entity
    """
    def get(self):
        query = User.query.all()
        return {
                'status': 'OK',
                'users': [item.serialized for item in query]
        }
    
    def post(self):
        login = request.json.get('login')
        email = request.json.get('email')
        role = request.json.get('role') or 1            # Defaults to trainee role
        current_app.logger.debug(
            f"Got POST request on /users with parameters:\n"
            f"   login={login}, email={email}, role={role}"
        )
        
        if login is None or email is None:
            abort(400, description="The data set you specified lacks required fields.")

        try:
            new_user = User(login=login, email=email, role=role)
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            abort(401, description="User already exists.")
        else:
            current_app.logger.debug(f"Created user id {new_user.id}")
            return {
                       'status': 'OK',
                       'user': new_user.serialized
                   }, 201
