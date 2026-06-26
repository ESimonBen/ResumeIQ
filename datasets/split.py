# split.py
from sklearn.model_selection import train_test_split

def split_dataset(df, train=0.8, val=0.1, test=0.1):
    df = df[df["label"] != "OTHER"]

    train_df, temp = train_test_split(
        df,
        test_size=(1 - train),
        stratify=df["label"],
        random_state=42
    )

    val_ratio = test / (val + test)
    val_df, test_df = train_test_split(
        temp,
        test_size = val_ratio,
        stratify=temp["label"],
        random_state=42
    )

    return train_df, val_df, test_df