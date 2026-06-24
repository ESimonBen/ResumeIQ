# labeling.py

DOMAINS = [
    "TECHNICAL",
    "NON_TECHNICAL",
    "HEALTHCARE",
    "LEGAL",
    "GOVERNMENT",
]

SUBCLASSES = {
    "TECHNICAL": {
        "Software Engineering": ["software", "backend", "frontend", "api"],
        "IT Support": ["help desk", "support", "troubleshooting"],
        "Cybersecurity": ["security", "cyber", "vulnerability"],
        "Data / Analytics": ["data", "sql", "python", "analytics"],
    },

    "NON_TECHNICAL": {
        "HR": ["human resources", "recruitment"],
        "Finance": ["budget", "accounting", "finance"],
        "Admin": ["assistant", "clerk", "office"],
    },

    "GOVERNMENT": {
        "Policy": ["policy", "regulation", "legislation"],
        "Program Management": ["program", "project", "management"],
        "Intelligence": ["intelligence", "security clearance"],
    },

    "HEALTHCARE": {
        "Clinical": ["nurse", "physician", "clinical"],
        "Public Health": ["epidemiology", "health policy"],
        "Lab Sciences": ["laboratory", "specimen"],
    },

    "LEGAL": {
        "Litigation": ["litigation", "court", "case law"],
        "Compliance": ["compliance", "regulation"],
        "Legal Research": ["legal research", "briefing"],
    }
}

# KEYWORDS = {
#     "TECHNICAL": {
#         "title": ["software", "developer", "engineer", "cybersecurity", "cloud"],
#         "text": ["python", "java", "api", "backend", "linux", "sql"]
#     },
#
#     "HEALTHCARE": {
#         "title": ["nurse", "physician", "medical", "clinical"],
#         "text": ["patient", "hospital", "health", "diagnosis"]
#     },
#
#     "LEGAL": {
#         "title": ["attorney", "law", "legal", "compliance"],
#         "text": ["litigation", "regulation", "case law"]
#     },
#
#     "GOVERNMENT_SPECIALIZED": {
#         "title": ["program analyst", "policy", "intelligence"],
#         "text": ["grant", "federal", "public affairs", "mission"]
#     },
#
#     "NON_TECHNICAL": {
#         "title": ["assistant", "clerk", "hr", "finance", "budget"],
#         "text": ["procurement", "accounting", "administration"]
#     }
# }

# def score_job(row):
#     title = row.get("title", "").lower()
#     text = row.get("description", "").lower()
#
#     scores = {label: 0 for label in KEYWORDS}
#
#     for label, groups in KEYWORDS.items():
#         for kw in groups["title"]:
#             if kw in title:
#                 scores[label] += 5
#
#         for kw in groups["text"]:
#             if kw in text:
#                 scores[label] += 2
#
#         return scores

def predict_domain(row):
    title = row.get("title", "").lower()
    text = row.get("description", "").lower()

    scores = {
        "TECHNICAL": 0,
        "NON_TECHNICAL": 0,
        "HEALTHCARE": 0,
        "LEGAL": 0,
        "GOVERNMENT": 0,
    }

    # strong signals only
    if any(k in title for k in ["software", "developer", "engineer"]):
        scores["TECHNICAL"] += 5

    if any(k in title for k in ["nurse", "medical", "physician"]):
        scores["HEALTHCARE"] += 5

    if any(k in title for k in ["attorney", "law", "legal"]):
        scores["LEGAL"] += 5

    if any(k in title for k in ["policy", "program analyst", "government"]):
        scores["GOVERNMENT"] += 5

    if any(k in title for k in ["assistant", "clerk", "hr", "finance"]):
        scores["NON_TECHNICAL"] += 5

    return max(scores, key=scores.get)

def predict_subclass(row, domain):
    title = row.get("title", "").lower()
    text = row.get("description", "").lower()

    candidates = SUBCLASSES.get(domain, {})

    if not candidates:
        return "UNKNOWN"

    scores = {label: 0 for label in candidates}

    for label, keywords in candidates.items():
        for kw in keywords:
            if kw in title:
                scores[label] += 5
            if kw in text:
                scores[label] += 2

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return "UNKNOWN"

    return best

def label_job(row):
    domain = predict_domain(row)
    subclass = predict_subclass(row, domain)

    return domain

def debug_job(job):
    label = label_job(job)

    print("\n---")
    print(job["title"])
    print(label)

    return label