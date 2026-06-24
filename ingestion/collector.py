# collector.py
from ingestion.usajobs_client import USAJobsClient

class JobCollector:
    def __init__(self, client : USAJobsClient):
        self.client = client
        self.seen_ids = set()

    def collect(self, keywords, max_pages=5):
        all_jobs = []

        for keyword in keywords:
            print(f"Fetching: {keyword}")
            raw_jobs = self.client.fetch_keyword(keyword, max_pages=max_pages)

            for job in raw_jobs:
                job_id = job["MatchedObjectDescriptor"].get("PositionID")

                if job_id in self.seen_ids:
                    continue

                self.seen_ids.add(job_id)
                all_jobs.append(job)

        return all_jobs