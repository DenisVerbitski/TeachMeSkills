import os


class Config(object):
    PATH = "/usr/logs"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True