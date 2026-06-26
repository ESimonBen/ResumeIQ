# data_transformer.py
import re

class DatasetTransformer:
    def __init__(self):
        pass

    def clean_text(self, text):
        if not text:
            return ""

        text = str(text).lower()
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def transform(self, df):
        df = df.copy()

        for col in ["title", "description", "company", "location"]:
            df[col] = df[col].fillna("").apply(self.clean_text)

        df["text"] = (
            df["title"] + " " +
            df["company"] + " " +
            df["location"] + " " +
            df["description"]
        )

        df["text"] = df["text"].apply(self.clean_text)

        return df