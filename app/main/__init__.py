from flask import Flask
import redis

from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    if not app.testing:
        redis_client = init_clients(app, app.config['SETTINGS'])
        app.redis_client = redis_client

    return app


def init_clients(app, app_settings):
    if not app.debug:
        redis_client = redis.StrictRedis(
            host=app_settings['REDIS_HOST'],
            port=app_settings['REDIS_PORT']
        )
    else:
        redis_client = redis.Redis(
            host=app_settings['REDIS_HOST'],
            port=app_settings['REDIS_PORT']
        )


    return redis_client
