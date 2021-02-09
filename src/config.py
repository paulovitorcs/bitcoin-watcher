from os import environ

class DefaultConfig:
    APP_NAME = environ.get('APP_NAME', default='Basic Python Starter')
    PUSHOVER_TOKEN = environ.get('PUSHOVER_TOKEN')
    PUSHOVER_USER = environ.get('PUSHOVER_USER')
    DEBUG = False

class Development(DefaultConfig):
    DEBUG = True

class Production(DefaultConfig):
    ...

class Testing(DefaultConfig):
    TESTING=True

def get_env(env = None):
    envs = {
        'default': DefaultConfig,
        'development': Development,
        'production': Production,
        'testing': Testing
    }

    selected_env = env if env != None else environ.get('Env', default='production')
    return envs[selected_env]

env = get_env()