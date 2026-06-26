# collect_jobs.py
from database.db import Database
from ingestion.loader import insert_jobs
from ingestion.collector import JobCollector
from ingestion.sources.usajobs import USAJobsSource
from ingestion.sources.theirstack import TheirStackSource
from ingestion.sources.adzuna import AdzunaSource

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
    sources = [
        USAJobsSource(),
        #TheirStackSource(),
        AdzunaSource()
    ]

    collector = JobCollector(sources=sources)

    print("Collecting jobs...")

    jobs = collector.collect(KEYWORDS, max_pages=20)

    print(f"Collected {len(jobs)} jobs")

    preview_jobs(jobs)

    db = Database()
    db.init()

    insert_jobs(jobs)

    print("Ingestion complete -> Jobs now stored in database")

if __name__ == "__main__":
    main()