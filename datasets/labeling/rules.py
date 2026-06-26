# rules.py
DOMAINS = [
    "TECHNICAL",
    "BUSINESS",
    "GOVERNMENT",
    "HEALTHCARE",
    "LEGAL",
    "EDUCATION",
    "SCIENCE",
    "SKILLED_TRADES",
    "OTHER",
    "UNKNOWN"
]

DOMAIN_RULES = {
    "TECHNICAL": {
        "title": [
            "software engineer",
            "software developer",
            "developer",
            "programmer",
            "computer scientist",
            "cybersecurity",
            "data scientist",
            "machine learning",
            "systems engineer",
            "network engineer",
            "cloud engineer",
            "devops",
            "site reliability",
            "database administrator",
            "it specialist",
            "help desk"
        ],

        "text": [
            "python",
            "java",
            "c++",
            "sql",
            "aws",
            "azure",
            "linux",
            "docker",
            "kubernetes",
            "tensorflow",
            "pytorch",
            "api",
            "backend",
            "frontend"
        ]
    },

    "BUSINESS": {
        "title": [
            "human resources",
            "finance",
            "accountant",
            "analyst",
            "marketing",
            "sales",
            "project manager",
            "program manager",
            "business analyst",
            "operations",
            "administrator"
        ],

        "text": [
            "budget",
            "recruitment",
            "procurement",
            "customer service",
            "financial",
            "business strategy"
        ]
    },

    "GOVERNMENT": {
        "title": [
            "program analyst",
            "policy analyst",
            "management analyst",
            "intelligence analyst",
            "public affairs",
            "contract specialist",
            "grants specialist"
        ],

        "text": [
            "federal",
            "agency",
            "government",
            "grant",
            "public",
            "mission",
            "clearance"
        ]
    },

    "HEALTHCARE": {
        "title": [
            "nurse",
            "physician",
            "medical officer",
            "medical assistant",
            "health scientist",
            "pharmacist",
            "psychologist",
            "psychiatrist",
        ],

        "text": [
            "patient",
            "clinical",
            "hospital",
            "diagnosis",
            "healthcare",
            "medical",
            "mental health"
        ]
    },

    "LEGAL": {
        "title": [
            "attorney",
            "law",
            "paralegal",
            "judge",
            "legal counsel",
            "compliance"
        ],

        "text": [
            "court",
            "litigation",
            "legal research",
            "regulation",
            "criminal",
            "civil"
        ]
    },

    "EDUCATION": {
        "title": [
            "teacher",
            "professor",
            "instructor",
            "faculty"
        ],

        "text": [

            "curriculum",
            "students",
            "education",
            "classroom"
        ]
    },

    "SCIENCE": {
        "title": [
            "chemist",
            "biologist",
            "physicist",
            "research scientist"
        ],

        "text": [
            "laboratory",
            "research",
            "experiments"
        ]
    },

    "SKILLED_TRADES": {
        "title": [
            "electrician",
            "mechanic",
            "plumber",
            "technician",
            "welder"
        ],

        "text": [
            "repair",
            "maintenance",
            "installation"
        ]
    }
}


