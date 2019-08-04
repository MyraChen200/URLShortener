DB = {
    "dbhost": '127.0.0.1:3306',
    "dbuser": 'myra',
    "dbpass": 'gomyra',
    "dbname": 'URLShortener'
}
DB_URI = 'mysql://{0[dbuser]}:{0[dbpass]}@{0[dbhost]}/{0[dbname]}'.format(DB)

class Config(object):
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
