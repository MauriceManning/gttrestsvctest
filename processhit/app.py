import json

import falcon

from processhit import ProcessHit

api = application = falcon.API()

phit = ProcessHit()

api.add_route('/processhit', phit)
