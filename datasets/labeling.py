# labeling.py

DOMAINS = [
    "TECHNICAL",
    "NON_TECHNICAL",
    "HEALTHCARE",
    "LEGAL",
    "GOVERNMENT",
]

DOMAIN_KEYWORDS = {
    "TECHNICAL": {
        "title": [
            "software engineer",
            "developer",
            "programmer",
            "it specialist",
            "cybersecurity",
            "data scientist"
        ],
        "text": [
            "python",
            "java",
            "sql",
            "cloud",
            "aws",
            "linux"
        ]
    },

    "NON_TECHNICAL": {
        "title": [
            "assistant",
            "administrator",
            "finance specialist",
            "human resources"
        ],
        "text": [
            "accounting",
            "budget",
            "procurement",
            "recruitment"
        ]
    },

    "HEALTHCARE": {
        "title": [
            "nurse",
            "physician",
            "medical officer",
            "health scientist"
        ],
        "text": [
            "patient",
            "clinical",
            "hospital",
            "diagnosis",
            "healthcare"
        ]
    },

    "LEGAL": {
        "title": [
            "attorney",
            "law",
            "paralegal",
            "judge",
            "prosecutor",
            "public defender",
            "legal counsel",
            "compliance officer",
            "magistrate"
        ],
        "text": [
            "litigation",
            "legal research",
            "court",
            "case law",
            "compliance",
            "regulation",
            "prosecution",
            "defense",
            "criminal law",
            "civil law"
        ]
    },

    "GOVERNMENT": {
        "title": [
            "program analyst",
            "policy analyst",
            "intelligence analyst"
        ],
        "text": [
            "federal",
            "grant",
            "mission",
            "public affairs",
            "government"
        ]
    }
}

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
        "Attorney": ["attorney", "defense", "prosecution"],
    }
}

def predict_domain(row):
    title = row.get("title", "").lower()
    text = row.get("description", "").lower()

    scores = {domain: 0 for domain in DOMAIN_KEYWORDS}

    for domain, groups in DOMAIN_KEYWORDS.items():

        for kw in groups["title"]:
            if kw in title:
                scores[domain] += 5

        for kw in groups["text"]:
            if kw in text:
                scores[domain] += 2

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return "UNKNOWN"

    return best

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