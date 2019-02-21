import os

# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xea\x8d\xa2%\x140U\x85?\xfb\x1fX\xf2(n\xcdg\xa4OBm\xe0x8'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
