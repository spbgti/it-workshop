from flask import request, current_app
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError

from workshop.database import db
from workshop.models.project import Project


class ProjectsListAPI(Resource):
    """
    API Resource class for Project entity
    """
    def get(self):
        query = Project.query.all()
        return {
                'status': 'OK',
                'projects': [item.serialized for item in query]
        }
    
    def post(self):
        name = request.json.get('name')
        description = request.json.get('description')
        author_id = request.json.get('author_id')
        current_app.logger.debug(
            f"Got POST request on '/projects' with parameters:\n"
            f"   name={name}, description={description}, author_id={author_id}"
        )
        
        if name is None or author_id is None:
            abort(400, description="The data set you specified lacks required fields.")

        try:
            new_project = Project(name=name, description=description, author_id=author_id, stage='proposed')
            db.session.add(new_project)
            db.session.commit()
        except IntegrityError:
            abort(401, description="The author ID you specified is nowhere to be found.")
        else:
            current_app.logger.debug(f"Created project id {new_project.id}")
            return {
                       'status': 'OK',
                       'project': new_project.serialized
                   }, 201
