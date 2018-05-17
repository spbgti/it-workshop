DOMAIN = {
    'projects': {
        'schema': {
            'title': {},
            'description': {},
            'commands': {},
            'mentors': {},
            'companies': {}
        }
    },
    'teams': {
        'schema': {
            'people_ids': {
                'type': 'list',
                'data_relation': {
                     'resource': 'people',
                     'field': '_id',
                },
            }
        }
    },
    'people': {
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
                'empty': False,
            },
            'skills': {
                'type': 'list',
            }
        }
    },
    'companies': {}
}

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
RENDERERS = ['eve.render.JSONRenderer']