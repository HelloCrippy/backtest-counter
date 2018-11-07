import logging
from functools import wraps

logging.basicConfig(
    format='%(asctime)s ~ %(levelname)-10s %(name)-25s %(message)s',
    datefmt='%Y-%m-%d %H:%M', level=logging.DEBUG)  # , filename='*.log')

logging.getLogger('boto3').setLevel(logging.INFO)
logging.getLogger('botocore').setLevel(logging.INFO)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)

logging.addLevelName(logging.DEBUG, '🐛 DEBUG')
logging.addLevelName(logging.INFO, '📑 INFO')
logging.addLevelName(logging.WARNING, '🤔 WARNING')
logging.addLevelName(logging.ERROR, '🚨 ERROR')


def get_logger(name):
    return logging.getLogger(name)


def log(show_params=True, show_result=False):
    def wrapped(func):
        logger = logging.getLogger(func.__module__)
        
        @wraps(func)
        def inner_wrapped(*args, **kwargs):
            log_str = f"{func.__name__}() is called "
            if show_params:
                log_str += f"with params {args} and {kwargs} "
            logger.debug(log_str)

            result = func(*args, **kwargs)
            if show_result:
                logger.debug(f"{func.__name__}() returned {result} ")
            return result
        
        return inner_wrapped
    return wrapped
