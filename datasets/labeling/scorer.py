# scorer.py
from datasets.labeling.rules import DOMAIN_RULES

TITLE_WEIGHT = 5
TEXT_WEIGHT = 2

class RuleScorer:
    def __init__(self):
        pass

    def score_domain(self, text: str, title: str):
        scores = {d: 0 for d in DOMAIN_RULES}

        for domain, rules in DOMAIN_RULES.items():
            for kw in rules["title"]:
                if kw in title:
                    scores[domain] += TITLE_WEIGHT

            for kw in rules["text"]:
                if kw in text:
                    scores[domain] += TEXT_WEIGHT

        return scores

    def best_label(self, scores: dict):
        best = max(scores, key=scores.get)

        if scores[best] == 0:
            return "OTHER", 0.0

        total = sum(scores.values())
        confidence = scores[best] / total if total > 0 else 0.0

        return best, confidence