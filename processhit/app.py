import json
import falcon
from processhit import ProcessHit

api = application = falcon.API()

phit = ProcessHit()

# curl http://localhost:8000/processhit 
api.add_route('/processhit', phit)
