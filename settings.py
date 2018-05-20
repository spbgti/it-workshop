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
MONGO_URI = os.environ.get('MONGODB_URI','mongodb://localhost:27017/eve')