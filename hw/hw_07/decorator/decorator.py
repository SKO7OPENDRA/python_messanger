import sys
import inspect
from log_config.client_log_config import CLIENT_LOGGER
from log_config.server_log_config import SERVER_LOGGER
from functools import wraps
sys.path.append('../')


def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        res = func(*args, **kwargs)
        CLIENT_LOGGER.debug(
            'Функция {} вызвана из {}'.format(
                func.__name__,
                inspect.stack()[1][3]))
        CLIENT_LOGGER.debug(
            'Функция {}({}, {}), возвращает {}'.format(
                func.__name__, args, kwargs, res))
        SERVER_LOGGER.debug(
            'Функция {} вызвана из {}'.format(
                func.__name__,
                inspect.stack()[1][3]))
        SERVER_LOGGER.debug(
            'Функция {}({}, {}), возвращает {}'.format(
                func.__name__, args, kwargs, res))
        return res
    return call
