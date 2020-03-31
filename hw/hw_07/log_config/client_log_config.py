import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler
sys.path.append('../')

CLIENT_LOGGER = logging.getLogger('client')

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(module)s %(message)s ")

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, '../log/client.log')

LOG_FILE = TimedRotatingFileHandler(
    PATH,
    when="midnight",
    backupCount=13,
    encoding='utf-8')
LOG_FILE.setLevel(logging.DEBUG)
LOG_FILE.setFormatter(formatter)

CLIENT_LOGGER.addHandler(LOG_FILE)
CLIENT_LOGGER.setLevel(logging.DEBUG)
