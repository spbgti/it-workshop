from workshop.database import db
from workshop.models.user import User


class Project(db.Model):
    """
    Database model for `project` entity.
    
    Attributes:
        id:             Numerical identificator used by the database
        name:           Project's name string.
        description:    Project's description as defined by user.
        stage:          Lifecycle stage of the project.
        author_id:      Numeric ID of author's `User` object
        author:         Direct join of author's `User` object as per `author_id`
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(500))
    stage = db.Column(db.String(50))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship(User, primaryjoin=author_id == User.id)

    def __init__(self, name: str, description: str, author_id: int):
        """Initializes Project class with data"""
        self.name = name
        self.description = description
        self.author_id = author_id

    def __repr__(self):
        """Prints correct Python representation of the Project class"""
        return f"<Project {self.id} '{self.name}', author id {self.author_id}"
