# loader.py
from database.db import Database

def insert_jobs(jobs):
    db = Database()

    query = """
    INSERT OR IGNORE INTO jobs
    (id, title, company, location, description, source, date_posted)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    for job in jobs:
        db.execute(query, (
            job["id"],
            job["title"],
            job["company"],
            job["location"],
            job["description"],
            job["source"],
            job["date_posted"]
        ))