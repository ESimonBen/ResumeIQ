# checks.py

class DatasetChecks:
    def __init__(self, df):
        self.df = df

    def rare_labels(self, threshold=5):
        counts = self.df["label"].value_counts()

        return counts[counts < threshold]

    def short_texts(self, min_length=20):
        return self.df[self.df["text"].str.len() < min_length]

    def empty_descriptions(self):
        return self.df[self.df["description"].str.strip() == ""]