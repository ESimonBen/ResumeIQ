# labeling.py

LABELS = [
    "Computer Science / IT",
    "Engineering",
    "Business / Finance",
    "Healthcare / Life Sciences",
    "Legal / Policy",
    "Administrative / Human Resources",
    "Government Operations",
    "Other"
]

TITLE_KEYWORDS = {
    "Computer Science / IT": [
        "software",
        "developer",
        "computer scientist",
        "cyber",
        "it specialist",
        "information technology",
        "systems administrator"
    ],

    "Engineering": [
        "engineer",
        "civil",
        "mechanical",
        "electrical",
        "environmental",
        "industrial",
        "architect"
    ],

    "Business / Finance": [
        "accountant",
        "budget",
        "financial",
        "economist",
        "contract",
        "business"
    ],

    "Healthcare / Life Sciences": [
        "health",
        "nurse",
        "biologist",
        "laboratory",
        "medical",
        "scientist"
    ],

    "Legal / Policy": [
        "law",
        "attorney",
        "paralegal",
        "policy",
        "legislative"
    ],

    "Administrative / Human Resources": [
        "administrative",
        "human resources",
        "office",
        "assistant",
        "clerk"
    ],

    "Government Operations": [
        "program analyst",
        "management analyst",
        "public affairs",
        "intelligence",
        "emergency management"
    ]
}

DESCRIPTION_KEYWORDS = {
    "Computer Science / IT": [
        "python",
        "java",
        "javascript",
        "c++",
        "sql",
        "database",
        "linux",
        "windows server",
        "network",
        "networking",
        "cybersecurity",
        "information security",
        "cloud",
        "aws",
        "azure",
        "docker",
        "git",
        "software development",
        "web development",
        "application development",
        "api",
        "troubleshooting",
        "technical support",
        "help desk",
        "system administration",
        "active directory"
    ],

    "Engineering": [
        "cad",
        "autocad",
        "solidworks",
        "engineering design",
        "technical drawings",
        "structural analysis",
        "quality assurance",
        "manufacturing",
        "testing",
        "electrical systems",
        "mechanical systems",
        "civil engineering",
        "environmental engineering",
        "construction",
        "project engineering",
        "safety standards",
        "engineering principles",
        "materials",
        "design review",
        "field inspections"
    ],

    "Business / Finance": [
        "budget",
        "budgeting",
        "accounting",
        "financial analysis",
        "financial reporting",
        "procurement",
        "contracts",
        "acquisition",
        "auditing",
        "compliance",
        "cost analysis",
        "forecasting",
        "spreadsheet",
        "excel",
        "bookkeeping",
        "invoice",
        "expense tracking",
        "economics",
        "market research",
        "business operations"
    ],

    "Healthcare / Life Sciences": [
        "patient care",
        "clinical",
        "medical",
        "nursing",
        "public health",
        "health education",
        "epidemiology",
        "biology",
        "biological",
        "microbiology",
        "laboratory",
        "specimen",
        "health policy",
        "research study",
        "health sciences",
        "life sciences",
        "disease prevention",
        "healthcare",
        "pharmaceutical",
        "veterinary"
    ],

    "Legal / Policy": [
        "legal research",
        "policy analysis",
        "legislation",
        "regulatory",
        "compliance review",
        "case law",
        "litigation",
        "paralegal",
        "attorney",
        "memoranda",
        "briefing",
        "government ethics",
        "rulemaking",
        "statute",
        "administrative law",
        "legal writing",
        "public policy",
        "regulations",
        "hearings",
        "investigation"
    ],

    "Administrative / Human Resources": [
        "administrative support",
        "office administration",
        "human resources",
        "recruitment",
        "staffing",
        "onboarding",
        "scheduling",
        "customer service",
        "records management",
        "filing",
        "correspondence",
        "data entry",
        "calendar management",
        "travel coordination",
        "payroll",
        "training coordination",
        "employee relations",
        "clerical",
        "office procedures",
        "document preparation"
    ],

    "Government Operations": [
        "program management",
        "program evaluation",
        "program analyst",
        "management analyst",
        "public affairs",
        "stakeholder engagement",
        "grant administration",
        "emergency management",
        "homeland security",
        "intelligence",
        "mission support",
        "strategic planning",
        "government operations",
        "performance metrics",
        "policy implementation",
        "interagency coordination",
        "federal regulations",
        "report preparation",
        "administration",
        "operational support"
    ]
}

def label_job(row):
    title = row.get("title", "").lower()
    text = row.get("description", "").lower()

    scores = {label: 0 for label in LABELS}

    for label, keywords in TITLE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in title:
                scores[label] += 5

    for label, keywords in DESCRIPTION_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                scores[label] += 1

    # fallback
    best = max(scores, key=scores.get)

    return best if scores[best] > 0 else "Other"

def debug_job(job):
    label = label_job(job)

    print("\n---")
    print(job["title"])
    print(label)

    return label