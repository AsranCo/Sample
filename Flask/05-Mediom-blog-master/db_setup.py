import sqlite3
from server import db_handler

try:
    conn = db_handler.create_connection()
    cur = conn.cursor()


    cur.execute('''
        CREATE TABLE IF NOT EXISTS User(
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
     ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Post(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER REFERENCES User
     )''')

    conn.commit()
    conn.close()

except Exception as e:
    print(e)
