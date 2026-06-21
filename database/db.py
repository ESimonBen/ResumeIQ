# db.py
import sqlite3
from database.schema import JOBS_TABLE_SQL
from config.paths import DB_PATH


class Database:
    def __init__(self):
        self.db_path = DB_PATH

    def connect(self):
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        return conn

    def init(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(JOBS_TABLE_SQL)
            conn.commit()

    def execute(self, query, params=None):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or [])
            conn.commit()

    def fetch_all(self, query, params=None):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or [])
            return cursor.fetchall()