from flask import request, current_app
from flask_restful import Resource, abort

from workshop.database import db
from workshop.models.project import Project


class ProjectsListApi(Resource):
    """
    API Resource class for Project entity
    """
    def get(self):
        query = Project.query.all()
        return {
                'status': 'OK',
                'projects': [i.serialized for i in query]
        }
    
    def post(self):
        name = request.json['name'] or None
        description = request.json['description'] or None
        author_id = request.json['author_id'] or None
        current_app.logger.debug(
            f"Got POST request on '/projects' with parameters:\n"
            f"   name={name}, description={description}, author_id={author_id}"
        )
        
        if name is None or author_id is None:
            abort(400)              # TODO: Give proper description of what has gone wrong

        new_item = Project(name=name, description=description, author_id=author_id, stage='proposed')
        db.session.add(new_item)
        db.session.commit()
        
        if new_item.id is not None:
            current_app.logger.debug(
                f"Created Project id {new_item.id}"
            )
            return {
                    'status': 'OK',
                    'project': new_item.serialized
            }, 201
        else:
            abort(500)          # Something really fucked up
