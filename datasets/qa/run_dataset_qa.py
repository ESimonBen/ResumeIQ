# run_dataset_qa.py
import pandas as pd
from config.paths import PROCESSED_DIR
from datasets.qa.analyzer import DatasetAnalyzer
from datasets.qa.checks import DatasetChecks
from datasets.qa.reporting import DatasetReporter

def main():
    train = pd.read_csv(PROCESSED_DIR / "train.csv")

    analyzer = DatasetAnalyzer(train)
    checks = DatasetChecks(train)

    reporter = DatasetReporter(analyzer)

    reporter.print_summary()

    print("\nRare Labels:")
    print(checks.rare_labels())

    print("\nShort Text Examples:")
    print(checks.short_texts().head())

if __name__ == "__main__":
    main()