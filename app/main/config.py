import os
import yaml

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    with open(r'app/main/settings_dev.yaml') as file:
        SETTINGS = yaml.load(file, Loader=yaml.FullLoader)


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    with open(r'app/main/settings_test.yaml') as file:
        SETTINGS = yaml.load(file, Loader=yaml.FullLoader)


class ProductionConfig(Config):
    DEBUG = False
    with open(r'app/main/settings_prod.yaml') as file:
        SETTINGS = yaml.load(file, Loader=yaml.FullLoader)


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
