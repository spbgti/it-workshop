projects = {
    'schema': {
        'title': {
            'type': 'string',
        },
        'short_description': {
            'type': 'string',
        },
        'link': {
            'type': 'string',
        },
        'source': {
            'type': 'string',
        },
        'description': {
            'type': 'string',
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
        },
        #'companies': {}
    },
    'datasource': {
        'default_sort': [('_created', -1)]
    }
}