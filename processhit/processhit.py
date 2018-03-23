import logging
import json
import falcon

class ProcessHit(object):

    # set up logging to file
    # '/code/logs/gtt.log' : '/Users/mauricemanning/Dev/code/gtt/logs/gtt.log'
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(funcName)s():  %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename='/code/logs/gtt.log',
                    filemode='w')
	
    def on_get(self, req, resp):
        print('-- on_get')
        logging.debug('-- on_get')
        payload = {'foo':'bar'}
        resp.body = json.dumps(payload)
        resp.status = falcon.HTTP_200
    

    def on_post(self, req, resp):	
        """Handles POST requests"""
        print('-- on_post')
        try:
            raw_json = req.stream.read()
            logging.info('on_post: ' + str(raw_json))
        except Exception as ex:
            logging.error('on_post: ' + ex.message)
