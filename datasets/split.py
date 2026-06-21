# split.py
from sklearn.model_selection import train_test_split

def validate_dataset(df):
    if "label" not in df.columns:
        raise ValueError("Dataset must contain 'label' column")

    if df["label"].isnull().any():
        raise ValueError("Null values found in label column")

    label_counts = df["label"].value_counts()

    rare_labels = label_counts[label_counts < 2]

    if len(rare_labels) > 0:
        print("\nWarning: Rare labels detected:")
        print(rare_labels)

def print_distribution(df, name):
    print(f"\n{name} distribution:")
    print(df["label"].value_counts())

def safe_train_test_split(df, test_size, stratify_col):
    """
    Falls back to non-stratified split if needed
    """

    try:
        return train_test_split(
            df,
            test_size=test_size,
            random_state=42,
            stratify=df[stratify_col]
        )
    except ValueError as e:
        print("\nStratified split failed, falling back to random split")
        print(str(e))

        return train_test_split(
            df,
            test_size=test_size,
            random_state=42
        )
def split_dataset(df, train_size=0.8, val_size=0.1, test_size=0.1):
    validate_dataset(df)

    if abs(train_size + val_size + test_size - 1.0) > 1e-6:
        raise ValueError("Split ratios must sum to 1.0")

    # Train vs Temp
    train_df, temp_df = safe_train_test_split(
        df,
        test_size=(1 - train_size),
        stratify_col="label"
    )

    # Val vs Test
    val_ratio_adjusted = test_size / (val_size + test_size)

    val_df, test_df = safe_train_test_split(
        temp_df,
        test_size=val_ratio_adjusted,
        stratify_col="label"
    )

    print_distribution(train_df, "Train")
    print_distribution(val_df, "Validation")
    print_distribution(test_df, "Test")

    return train_df, val_df, test_df