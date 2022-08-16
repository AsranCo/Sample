from os import urandom
class Config:
    SECRET_KEY = urandom(32).hex()
    DB = 'db_file.db'
