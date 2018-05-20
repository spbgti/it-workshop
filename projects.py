projects = {
    'schema': {
        'title': {
            'type': 'string',
            'required': True,
            'empty': False,
        },
        'short_description': {
            'type': 'string',
            'required': True,
            'empty': False,
        },
        'link': {
            'type': 'string',
            'required': True,
        },
        'progress': {
            'type': 'integer',
            'required': True,
            'empty': False,
        },
        'source': {
            'type': 'string',
            'required': True,
        },
        'full_description': {
            'type': 'string',
            'required': True,
        },
        'team': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'teams',
                'field': '_id',
            },
        },
        'mentors': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'people',
                    'field': '_id',
                    'embeddable': True
                },
            },
            'required': True,
        },
        'company': {
            'type': 'string',
            'required': True
        }
    },
    'datasource': {
        'default_sort': [('_created', -1)]
    }
}