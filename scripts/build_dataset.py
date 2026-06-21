# build_dataset.py
from datasets.builder import DatasetBuilder
from datasets.labeling import label_job
from datasets.split import split_dataset
from datasets.filter import DatasetFilter
from config.paths import PROCESSED_DIR

def main():
    builder = DatasetBuilder()
    filterer = DatasetFilter(min_label_samples=3)

    df = builder.build_dataset()

    # Labeling
    df["label"] = df.apply(label_job, axis=1)

    print("Raw label distribution:")
    filterer.print_distribution(df, "Raw dataset")

    # Filter
    df = filterer.filter_labels(df)

    print("\nFiltered label distribution:")
    filterer.print_distribution(df, "Filtered dataset")

    # Split
    train, val, test = split_dataset(df)

    # Save
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    train.to_csv(PROCESSED_DIR / "train.csv", index=False)
    val.to_csv(PROCESSED_DIR / "val.csv", index=False)
    test.to_csv(PROCESSED_DIR / "test.csv", index="False")

    print("\nDataset build complete")
    print(f"Train Size: {len(train)} | Val Size: {len(val)} | Test Size: {len(test)}")

if __name__ == "__main__":
    main()