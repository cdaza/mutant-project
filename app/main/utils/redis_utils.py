from functools import wraps
from flask import current_app


def execute_db_operation(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return None

    return wrapped


@execute_db_operation
def insert_key_value(key, value):
    current_app.redis_client.set(key, value)
    return True


def get_value_from_key(key):
    return current_app.redis_client.get(key)


def insert_key_dict(key, dict):
    current_app.redis_client.hmset(key, dict)
    return True


def get_dict_from_key(key):
    return current_app.redis_client.hgetall(key)
