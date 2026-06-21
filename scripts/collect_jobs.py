# collect_jobs.py
from ingestion.usajobs_client import USAJobsClient
from ingestion.transformer import transform_job
from ingestion.loader import insert_jobs
from database.db import Database

def preview_jobs(jobs, n=5):
    print(f"\nPreviewing {min(n, len(jobs))} jobs:\n")

    for job in jobs[:n]:
        print(job["title"])
        print(job["company"])
        print(job["location"])
        print("-" * 40)

def main():
    client = USAJobsClient()

    print("Fetching jobs from USAJobs API...")

    raw_jobs = client.fetch_all("intern", max_pages=10)

    print(f"Fetched {len(raw_jobs)} jobs")

    cleaned_jobs = [transform_job(job) for job in raw_jobs]

    print(f"Transformed {len(cleaned_jobs)} jobs")

    preview_jobs(cleaned_jobs)

    db = Database()
    db.init()

    insert_jobs(cleaned_jobs)

    print("Ingestion complete -> Jobs now stored in database")

if __name__ == "__main__":
    main()