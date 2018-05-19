people = {
    'schema': {
        'name': {
            'type': 'string',
            'required': True,
            'empty': False,
        },
        'skills': {
            'type': 'list',
        }
    },
    'datasource': {
        'default_sort': [('_created', -1)]
    }
}
