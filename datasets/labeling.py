# labeling.py

LABELS = [
    "Software Engineering",
    "Data Science / Analytics",
    "IT / Support",
    "Business / Finance",
    "Engineering",
    "Healthcare",
    "Government / Public Sector",
    "Other"
]


def label_job(row):
    title = row.get("title", "").lower()
    text = row.get("description", "").lower()

    scores = {label: 0 for label in LABELS}

    # -------------------------
    # SOFTWARE ENGINEERING
    # -------------------------
    if "software" in title or "developer" in title:
        scores["Software Engineering"] += 5

    if "api" in text or "backend" in text:
        scores["Software Engineering"] += 2

    # -------------------------
    # DATA / ANALYTICS
    # -------------------------
    if "data" in title or "analyst" in title:
        scores["Data Science / Analytics"] += 5

    if "sql" in text or "python" in text:
        scores["Data Science / Analytics"] += 1

    # -------------------------
    # IT
    # -------------------------
    if "it" in title or "support" in title:
        scores["IT / Support"] += 5

    if "helpdesk" in text:
        scores["IT / Support"] += 2

    # -------------------------
    # GOVERNMENT
    # -------------------------
    if "federal" in text or "government" in text:
        scores["Government / Public Sector"] += 2

    # fallback
    best = max(scores, key=scores.get)

    return best if scores[best] > 0 else "Other"

def debug_job(job):
    label = label_job(job)

    print("\n---")
    print(job["title"])
    print(label)

    return label