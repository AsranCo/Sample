import sqlite3
from server.config import Config
DB = Config.DB

conn = None


def create_connection(db_file=DB):
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn
