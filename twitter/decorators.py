import sys
import logging

logger = logging.getLogger(__name__)

def retry_if_fails(func):
    """
    Decorator retries function every time it fails
    """
    def inner(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
            except:
                logging.error(sys.exc_info()[0])
    return inner
