import logging

LOGGER = None

def setupLogger():
    LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
                      '-35s %(lineno) -5d: %(message)s')
    global LOGGER
    LOGGER = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def getLogger():
    global LOGGER
    return LOGGER
