class ProcessHit(object):

  

	def on_get(self, req, resp):
		payload = {}
    resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200
    
	def on_post(self, req, resp):
		payload = {}
