# schema.py

JOBS_TABLE_SQL = """
CREATE TABLE jobs (

    -- Identity
    id TEXT PRIMARY KEY,
    source_id TEXT,

    -- Job information
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,

    -- Processed text
    text_raw TEXT,
    text_clean TEXT,

    -- Labels
    domain TEXT,
    subclass TEXT,
    label_source TEXT,
    label_confidence REAL,

    -- Provenance
    source TEXT,
    search_keyword TEXT,
    date_posted TEXT,
    retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Original API response
    raw_json TEXT
);
"""