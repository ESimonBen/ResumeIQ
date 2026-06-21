# schema.py

JOBS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS jobs (
    id TEXT PRIMARY KEY,

    -- Core job fields
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,

    -- ML-ready fields (future-proofing)
    text_raw TEXT,
    text_clean TEXT,
    label TEXT,

    -- Data lineage (VERY important)
    source TEXT,
    search_keyword TEXT,
    date_posted TEXT,
    retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Debug / reproducibility
    raw_json TEXT
);
"""