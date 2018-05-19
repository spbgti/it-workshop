teams = {
    'schema': {
        'name': {
            'type': 'string',
            'required': True,
            'empty': False,
        },
        'people': {
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
            'empty': False,
        }
    },
    'datasource': {
        'default_sort': [('_created', -1)]
    }
}
