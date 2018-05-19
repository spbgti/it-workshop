from people import people
from projects import projects
from teams import teams

DOMAIN = {
    'projects': projects,
    'teams': teams,
    'people': people,
    'companies': {}
}

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
RENDERERS = ['eve.render.JSONRenderer']
X_DOMAINS = ['*']
X_HEADERS = ['*']
IF_MATCH = False
MONGO_QUERY_BLACKLIST = ['$where']
EMBEDDING = True