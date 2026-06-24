# pipeline.py
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from config.paths import PROCESSED_DIR, ARTIFACTS_DIR

class TrainingPipeline:
    def __init__(self):
        self.model = Pipeline([
            ("tfdif", TfidfVectorizer(
                max_features=10000,
                ngram_range=(1, 3),
                min_df=2,
                max_df=0.95,
                stop_words="english"
            )),
            ("clf", LogisticRegression(
                max_iter=1000,
                class_weight="balanced"
            ))
        ])

    def load_data(self):
        df = pd.read_csv(PROCESSED_DIR / "train.csv")
        val_df = pd.read_csv(PROCESSED_DIR / "val.csv")

        return df, val_df

    def train(self, train_df):
        self.model.fit(train_df["text"], train_df["label"])

    def evaluate(self, val_df):
        y_val = val_df["label"]

        preds = self.model.predict(val_df["text"])

        print(classification_report(y_val, preds))

    def save(self):
        ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

        joblib.dump(self.model, ARTIFACTS_DIR / "model.pkl")