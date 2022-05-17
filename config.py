class Config(object):
    DEBUG = False
    TESTING = False
    INIT_FIRST = False
    HOST = None
    USER = None
    DB = None
    PWD = None
    PORT = None
    
class Development(Config):
    DEBUG = True
    ENV_VALUE = "Development"
    INIT_FIRST = True
    HOST = "postgres"
    USER = "postgres"
    DB = "dev_database"
    PWD = "password"
    PORT = 5432

class Testing(Config):
    TESTING = True
    DEBUG = True
    INIT_FIRST = True
    ENV_VALUE = "Testing"
    HOST = "postgres"
    USER = "postgres"
    DB = "dev_database"
    PWD = "password"
    PORT = 5432
class Production(Config):
    DEBUG = False
    INIT_FIRST = True
    ENV_VALUE = "Production"
    HOST = "postgres"
    USER = "postgres"
    DB = "dev_database"
    PWD = "password"
    PORT = 5432