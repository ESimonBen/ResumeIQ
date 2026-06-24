# collect_jobs.py
from ingestion.usajobs_client import USAJobsClient
from ingestion.collector import JobCollector
from ingestion.transformer import transform_job
from ingestion.loader import insert_jobs
from database.db import Database

KEYWORDS = [
    "intern",
    "student",
    "trainee",
    "graduate",
    "fellowship",
    "entry level",
    "junior",
    "trainee program",
    "software intern",
    "data intern",
    "cybersecurity intern",
    "IT specialist",
    "budget analyst",
    "program analyst",
    "policy intern",
    "engineering intern"
]

def preview_jobs(jobs, n=5):
    print(f"\nPreviewing {min(n, len(jobs))} jobs:\n")

    for job in jobs[:n]:
        print(job["title"])
        print(job["company"])
        print(job["location"])
        print("-" * 40)

def main():
    client = USAJobsClient()
    collector = JobCollector(client)

    print("Collecting jobs...")

    raw_jobs = collector.collect(KEYWORDS, max_pages=10)

    print(f"Total unique jobs: {len(raw_jobs)}")

    cleaned_jobs = [transform_job(job) for job in raw_jobs]

    print(f"Transformed {len(cleaned_jobs)} jobs")

    preview_jobs(cleaned_jobs)

    db = Database()
    db.init()

    insert_jobs(cleaned_jobs)

    print("Ingestion complete -> Jobs now stored in database")

if __name__ == "__main__":
    main()