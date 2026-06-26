# predict.py
import joblib
from config.paths import ARTIFACTS_DIR

class JobClassifier:
    def __init__(self):
        self.model = joblib.load(ARTIFACTS_DIR / "model.pkl")

    def build_text(self, title: str, description: str) -> str:
        title = title or ""
        description = description or ""
        return f"{title} {description}".strip().lower()

    def predict(self, title: str, description : str):
        text = f"{title} {description}".lower()
        return self.model.predict([text])[0]

    def predict_proba(self, title: str, description: str):
        text = f"{title} {description}".lower()
        return self.model.predict_proba([text])[0]

    def predict_with_confidence(self, title: str, description: str):
        text = self.build_text(title, description)

        probs = self.model.predict_proba([text])[0]
        pred = self.model.predict([text])[0]

        confidence = max(probs)

        return {
            "label": pred,
            "confidence": float(confidence),
            "all_probs": probs.tolist()
        }