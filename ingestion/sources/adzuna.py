# adzuna.py
from ingestion.sources.base import JobSource
from ingestion.sources.adzuna_client import AdzunaClient

class AdzunaSource(JobSource):
    def __init__(self):
        self.client = AdzunaClient()

    def fetch(self, keywords, max_pages=5):
        all_jobs = []

        for keyword in keywords:
            raw_jobs = self.client.fetch_keyword(keyword, max_pages)

            all_jobs.extend(self.normalize(job) for job in raw_jobs)

        return all_jobs

    def normalize(self, raw_job):
        return {
            "id": f"adzuna_{raw_job.get('id')}",
            "source_id": raw_job.get("id"),
            "title": raw_job.get("title", ""),
            "company": (
                raw_job.get("company", {})
                .get("display_name", "")
            ),
            "location": (
                raw_job.get("location", {})
                .get("display_name", "")
            ),
            "description": raw_job.get("description", ""),
            "job_url": raw_job.get("redirect_url", ""),
            "source": "Adzuna",
            "search_keyword": None,
            "date_posted": raw_job.get("created"),
            "raw": raw_job
        }