# builder.py
import sqlite3
import pandas as pd
from config.paths import DB_PATH, DATASET_PATH

class DatasetBuilder:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    def load_raw_jobs(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql("SELECT * FROM jobs", conn)
        conn.close()
        return df

    def clean_text(self, text):
        if not text:
            return ""

        return text.lower().replace("\n", " ").strip()

    def clean_dataframe(self, df):
        df = df.copy()

        df["title"] = df["title"].fillna("").apply(self.clean_text)
        df["description"] = df["description"].fillna("").apply(self.clean_text)
        df["company"] = df["company"].fillna("").apply(self.clean_text)
        df["location"] = df["location"].fillna("").apply(self.clean_text)

        return df

    def build_text_features(self, df):
        df = df.copy()

        df["text"] = (
            df["title"] + " " +
            df["title"] + " " +
            df["description"]
        )

        df["text"] = df["text"].apply(self.clean_text)

        return df

    def filter_data(self, df):
        df = df.copy()

        # Remove empty rows
        df = df[df["text"].str.len() > 10]

        return df

    def build_dataset(self):
        df = self.load_raw_jobs()

        df = self.clean_dataframe(df)
        df = self.build_text_features(df)
        df = self.filter_data(df)

        return df[[
            "title",
            "company",
            "location",
            "description",
            "text"
        ]]

    def save_dataset(self, df, path=DATASET_PATH):
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)