# builder.py
import sqlite3
import pandas as pd
from config.paths import DB_PATH, DATASET_PATH

class DatasetBuilder:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    def load(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql("SELECT * FROM jobs", conn)
        conn.close()

        return df