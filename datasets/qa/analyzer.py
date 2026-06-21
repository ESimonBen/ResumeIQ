# analyzer.py

class DatasetAnalyzer:
    def __init__(self, df):
        self.df = df

    def label_distribution(self):
        return self.df["label"].value_counts()

    def label_percentages(self):
        counts = self.label_distribution()
        return counts / len(self.df) * 100

    def missing_values(self):
        return self.df.isnull().sum()

    def duplicate_count(self):
        return self.df.duplicated().sum()

    def text_lengths(self):
        lengths = self.df["text"].str.len()

        return {
            "mean": lengths.mean(),
            "median": lengths.median(),
            "min": lengths.min(),
            "max": lengths.max()
        }
