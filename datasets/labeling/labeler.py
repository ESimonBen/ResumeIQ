# labeler.py
from dataclasses import dataclass
from datasets.labeling.scorer import RuleScorer

@dataclass
class LabelResult:
    label: str
    confidence: float

class JobLabeler:
    def __init__(self):
        self.scorer = RuleScorer()

    def label_row(self, row):
        title = row.get("title", "")
        text = row.get("text", "")

        scores = self.scorer.score_domain(text, title)
        label, confidence = self.scorer.best_label(scores)

        return LabelResult(label, confidence)

    def label_dataframe(self, df):
        results = df.apply(self.label_row, axis=1)

        df = df.copy()

        df["label"] = [r.label for r in results]
        df["confidence"] = [r.confidence for r in results]

        return df
