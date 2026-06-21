# filter.py

class DatasetFilter:
    def __init__(self, min_label_samples=3):
        self.min_label_samples = min_label_samples

    def filter_labels(self, df):
        label_counts = df["label"].value_counts()

        valid_labels = label_counts[label_counts >= self.min_label_samples].index

        return df[df["label"].isin(valid_labels)]

    def print_distribution(self, df, title="Dataset"):
        print(f"\n{title} distribution:")
        print(df["label"].value_counts())