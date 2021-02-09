from os import environ

class DefaultConfig:
    DEBUG = False
    APP_NAME = environ.get('APP_NAME', default='Basic Python Starter')
    PUSHOVER_TOKEN = environ.get('PUSHOVER_TOKEN')
    PUSHOVER_USER = environ.get('PUSHOVER_USER')
    IS_TESTING=False

class Development(DefaultConfig):
    DEBUG = True

class Production(DefaultConfig):
    ...

class Testing(DefaultConfig):
    IS_TESTING=True
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