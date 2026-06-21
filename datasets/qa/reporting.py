# reporting.py

class DatasetReporter:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def print_summary(self):
        print("\nDATASET SUMMARY")

        print("\nLabel Distribution:")
        print(self.analyzer.label_distribution())

        print("\nMissing Values:")
        print(self.analyzer.missing_values())

        print("\nDuplicate Rows:")
        print(self.analyzer.duplicate_count())

        print("\nText Statistics:")
        print(self.analyzer.text_lengths())