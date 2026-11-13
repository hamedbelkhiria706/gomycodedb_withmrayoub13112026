import sqlite3
from contextlib import contextmanager
@contextmanager
def open_conn(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    try:
        yield conn
        print("connexion succeeded")
        conn.close()
        return conn
    except sqlite3.Error as e:
        print(f"failed to connect : {e}")
        return None
def select_all():
    with open_conn("app.db") as conn:
        cursor=conn.execute("""
        Select * FROM users
        """)
        rows=cursor.fetchall()
        print("rows")
        print(rows)
    
select_all()