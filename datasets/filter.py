# filter.py

class DatasetFilter:
    def __init__(self, min_label_samples=5, min_confidence=0.5):
        self.min_label_samples = min_label_samples
        self.min_confidence = min_confidence

    def filter_low_confidence(self, df):
        if "confidence" not in df:
            return df

        return df[df["confidence"] >= self.min_confidence]

    def filter_rare_labels(self, df):
        counts = df["label"].value_counts()
        valid = counts[counts >= self.min_label_samples].index

        return df[df["label"].isin(valid)]

    def apply_all(self, df):
        df = self.filter_low_confidence(df)
        df = self.filter_rare_labels(df)

        return df
