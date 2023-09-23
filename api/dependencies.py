import redis
from config import pool


def get_redis():
    return redis.Redis(connection_pool=pool)
