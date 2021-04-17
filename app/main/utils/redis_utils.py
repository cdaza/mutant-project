from flask import current_app


def insert_key_value(key, value):
    try:
        current_app.redis_client.set(key, value)
        return True
    except Exception as e:
        print(str(e))
        return False
