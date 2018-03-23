import logging
import pprint
from datetime import datetime
import os
import requests

from apscheduler.schedulers.blocking import BlockingScheduler

 
def sendraw():
    api_url = 'http://processhit:8000/processhit/'
    raw_data = {'id': '1235'}
    print(raw_data)
    logging.info('sendraw post...')
    try:
        r = requests.post(url=api_url, data=raw_data)
        logging.info('sendraw results: ' + str(r.status_code) + ' ' + str( r.reason) + ' ' +  str(r.text))
    except:
        logging.error('sendraw failed')

    try:
        api_url = 'http://processhit:8000/processhit/processhit'
        r = requests.post(url=api_url, data=raw_data)
        logging.info('sendraw results: ' + str(r.status_code) + ' ' + str( r.reason) + ' ' +  str(r.text))
    except:
        logging.error('sendraw failed')


def ingest():
    logging.info('ingest completed.')

    
if __name__ == '__main__':
    global logging
    
    # https://docs.python.org/3/howto/logging-cookbook.html
    # set up logging to file
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(funcName)s():  %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename='/code/logs/gtt.log',
                    filemode='w')

    # initial tests
    import time
    time.sleep(5)

    scheduler = BlockingScheduler()
    scheduler.add_job(sendraw, 'interval', seconds=30)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
       pass
