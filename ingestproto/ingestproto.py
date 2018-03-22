import logging
import pprint
from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler

 


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
    time.sleep(7)

    
    scheduler = BlockingScheduler()
    scheduler.add_job(ingest, 'interval', seconds=30)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
       pass