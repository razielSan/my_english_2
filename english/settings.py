import os

from dotenv import load_dotenv


load_dotenv()


path_db = os.path.join(os.getcwd(), 'english/english.db')
SERVER_NAME = os.getenv('SERVER_NAME')
DRIVER_DB = os.getenv("DRIVER_DB")
USER_DB = os.getenv("USER_DB")
PORT_DB = os.getenv("PORT_DB")
NAME_DB = os.getenv("NAME_DB")
PASSWORD_DB = os.getenv('PASSWORD_DB')


class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(32)
    TESTING = False
    TEMPLATES_AUTO_RELOAD = True


class ConfigDebug(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{path_db}'
    TESTING = True


class ConfigProd(Config):
    DEBUG = True
    PROPAGATE_EXCEPTIONS = bool(os.getenv('PROPAGATE_EXCEPTIONS'))
    SQLALCHEMY_DATABASE_URI = f'{DRIVER_DB}://{USER_DB}:{PASSWORD_DB}@{SERVER_NAME}:{PORT_DB}/{NAME_DB}'
