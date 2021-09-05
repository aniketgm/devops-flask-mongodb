import os

class Config(object):
    # SECRET_KEY = b'0\xfa\x1c|\xb0\x9a\xa5l\xc92\x10\xaf\xba\xfa\xb5\xfa'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DB_HOST = os.environ.get('DB_NAME') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or 27017
    DB_NAME = 'user_login'
