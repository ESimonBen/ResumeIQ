# builder.py
import re
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
        if pd.isna(text):
            return ""

        text = str(text)
        text = text.lower()
        text = text.replace("\n", " ")
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def clean_dataframe(self, df):
        df = df.copy()

        columns = [

            "title",
            "company",
            "location",
            "description"

        ]

        for column in columns:
            df[column] = (

                df[column]
                .fillna("")
                .apply(self.clean_text)

            )

        return df

    def normalize_dataframe(self, df):
        df = df.copy()

        df["source"] = df["source"].fillna("UNKNOWN")
        df["company"] = df["company"].replace("", "Unknown")

        return df

    def build_text(self, df):
        df = df.copy()

        df["text"] = (
            df["title"] + " " + df["company"] + " "
            + df["location"] + " " + df["description"]
        )

        df["text"] = df["text"].apply(self.clean_text)

        return df

    def remove_duplicates(self, df):
        return df.drop_duplicates(subset=["text"]).reset_index(drop=True)

    def filter_data(self, df):
        df = df.copy()

        # Remove empty rows
        df = df[df["text"].str.len() >= 20]
        df = df[df["title"].str.len() > 1]

        return df

    def build_text_features(self, df):
        df = df.copy()

        df["text"] = df.apply(self.build_text, axis=1)

        df["text"] = df["text"].apply(self.clean_text)

        return df

    def build_dataset(self):
        df = self.load_raw_jobs()

        df = self.clean_dataframe(df)
        df = self.normalize_dataframe(df)
        df = self.build_text_features(df)
        df = self.remove_duplicates(df)
        df = self.filter_data(df)

        return df

    def save_dataset(self, df, path=DATASET_PATH):
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)