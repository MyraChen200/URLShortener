# -- DB config
DB = {
    "dbhost": '127.0.0.1:3306',
    "dbuser": 'myra',
    "dbpass": 'gomyra',
    "dbname": 'URLShortener'
}

DB_URI = 'mysql://{0[dbuser]}:{0[dbpass]}@{0[dbhost]}/{0[dbname]}'.format(DB)

# -- Logging config
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(levelname)-5s][%(module)s][%(funcName)s():%(lineno)d]: %(message)s',
        }
    },
    'handlers': {
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'default',
            'filename': 'app.log'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['logfile']
    }
}

# -- env config setting
class Config(object):
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
