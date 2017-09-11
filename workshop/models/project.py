from workshop.database import db
from workshop.models.user import User


class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(500))
    stage = db.Column(db.String(50))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship(User, primaryjoin=author_id == User.id)

    def __init__(self, name: str, description: str, author_id: int):
        self.name = name
        self.description = description
        self.author_id = author_id

    def __repr__(self):
        return f"<Project {self.id} '{self.name}', author id {self.author_id}"
