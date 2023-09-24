import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def async_log_info():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            logger.info(f"START {func.__name__} with {args=} {kwargs=}")
            result = await func(*args, **kwargs)
            logger.info(f"END {func.__name__} as {result=}")
            return result
        return wrapped
    return wrapper