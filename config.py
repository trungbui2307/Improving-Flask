from distutils.debug import DEBUG


class Config(object):
    pass 

class ProdConfig(object):
    pass 

class DevConfig(object):
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_ECHO = True
   