from os import environ

class DefaultConfig:
    DEBUG = False
    APP_NAME = environ.get('APP_NAME', default='Basic Python Starter')
    PUSHOVER_TOKEN = environ.get('PUSHOVER_TOKEN')
    PUSHOVER_USER = environ.get('PUSHOVER_USER')
    INTERVAL = environ.get('PUSHOVER_USER', default=30)
    HAS_PUSHOVER = environ.get('PUSHOVER_USER', default=True)
    IS_TESTING=False

class Development(DefaultConfig):
    INTERVAL=1
    DEBUG = True

class Production(DefaultConfig):
    ...

class Testing(DefaultConfig):
    IS_TESTING=True
    HAS_PUSHOVER = False
    INTERVAL=1
    PUSHOVER_TOKEN = environ.get('PUSHOVER_TOKEN_TEST', default=DefaultConfig.PUSHOVER_TOKEN)
    PUSHOVER_USER = environ.get('PUSHOVER_USER_TEST', default=DefaultConfig.PUSHOVER_USER)

def get_env(env = None):
    envs = {
        'default': DefaultConfig,
        'development': Development,
        'production': Production,
        'testing': Testing
    }

    selected_env = env if env != None else environ.get('ENV', default='production')
    return envs[selected_env]

env = get_env()