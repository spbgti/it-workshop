from workshop.database import db


class User (db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    login = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(45), unique=True)
    role = db.Column(db.Integer)

    def __init__(self, login: str, email: str, role: int):
        self.login, self.email, self.role = login, email, role

    def __repr__(self):
        return f"<User {self.login} ({self.email}, role {self.role})>"