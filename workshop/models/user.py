from workshop.database import db


class User(db.Model):
    """
    Database model for `user` entity.
    
    Attributes:
        id:             Numerical identificator used by the database
        login:          Alphanumerical login string used for authentication
        email:          User's email address
        role:           Applicable community role (trainee/jedi/mentor)
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    login = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(45), unique=True)
    role = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.login} ({self.email}, role {self.role})>"
    
    @property
    def serialized(self):
        """Returns object data in serializable format"""
        return {
            'id': self.id,
            'login': self.login,
            'email': self.email,
            'role': self.role
        }
