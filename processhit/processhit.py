import logging

class ProcessHit(object):

    # set up logging to file
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(funcName)s():  %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename='/code/logs/gtt.log',
                    filemode='w')
	
    def on_get(self, req, resp):
        payload = {'foo':'bar'}
	resp.body = json.dumps(payload)
	resp.status = falcon.HTTP_200
    

    def on_post(self, req, resp):	
        """Handles POST requests"""
        try:
            raw_json = req.stream.read()
	    logging.info('on_post: ' + str(raw_json))
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)
