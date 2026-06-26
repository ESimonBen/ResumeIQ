# build_dataset.py
from config.paths import PROCESSED_DIR
from datasets.builder import DatasetBuilder
from datasets.data_transformer import DatasetTransformer
from datasets.labeling.labeler import JobLabeler
from datasets.filter import DatasetFilter
from datasets.split import split_dataset

def main():
    builder = DatasetBuilder()
    transformer = DatasetTransformer()
    labeler = JobLabeler()
    data_filter = DatasetFilter()

    df = builder.load()
    df = transformer.transform(df)
    df = labeler.label_dataframe(df)
    df = data_filter.apply_all(df)
    train, val, test = split_dataset(df)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    train.to_csv(PROCESSED_DIR / "train.csv", index=False)
    val.to_csv(PROCESSED_DIR / "val.csv", index=False)
    test.to_csv(PROCESSED_DIR / "test.csv", index=False)

    print("Done")
    print(len(train), len(val), len(test))

if __name__ == "__main__":
    main()