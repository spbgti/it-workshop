import os

from eve import Eve
from eve.auth import BasicAuth

import settings


class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == 'admin' and password == os.environ['IT_WORKSHOP_PASSWORD']

app = Eve(auth=MyBasicAuth)

if __name__ == '__main__':
    app.run(port=5001, debug=True)