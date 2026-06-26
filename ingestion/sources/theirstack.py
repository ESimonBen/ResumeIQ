# theirstack.py
from ingestion.sources.base import JobSource
from ingestion.sources.theirstack_client import TheirStackClient

class TheirStackSource(JobSource):
    def __init__(self):
        self.client = TheirStackClient()

    def fetch(self, keywords, max_pages=5):
        all_jobs = []

        for keyword in keywords:
            raw_jobs = self.client.fetch_keyword(keyword, max_pages)

            all_jobs.extend(self.normalize(job) for job in raw_jobs)

        return all_jobs

    def normalize(self, raw_job):
        return {
            "id": f"theirstack_{raw_job.get('id')}",
            "title": raw_job.get("title", ""),
            "company": raw_job.get("company", ""),
            "location": raw_job.get("location", ""),
            "description": raw_job.get("description", ""),
            "source": "TheirStack",
            "source_id": raw_job.get("id"),
            "date_posted": raw_job.get("date_posted"),
            "raw": raw_job
        }
