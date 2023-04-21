try:
    from .localsettings import *
except ImportError:
    pass

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT,
    DRIVER,
    DB_USER,
    DB_PWD,
    DB_HOST
    ,DB_PORT,
    DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True