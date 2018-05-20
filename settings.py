import os

from people import people
from projects import projects
from teams import teams

DOMAIN = {
    'projects': projects,
    'teams': teams,
    'people': people,
    'companies': {}
}

PUBLIC_METHODS = ['GET']
PUBLIC_ITEM_METHODS = ['GET']
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

RENDERERS = ['eve.render.JSONRenderer']
X_DOMAINS = ['*']
X_HEADERS = ['*']

IF_MATCH = False
EMBEDDING = True

MONGO_QUERY_BLACKLIST = ['$where']
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', None)
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', None)
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'eve')