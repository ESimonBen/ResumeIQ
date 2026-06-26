# usajobs.py
from ingestion.sources.base import JobSource
from ingestion.sources.usajobs_client import USAJobsClient

class USAJobsSource(JobSource):
    def __init__(self):
        self.client = USAJobsClient()

    def fetch(self, keywords, max_pages=5):
        all_jobs = []

        for keyword in keywords:
            raw_jobs = self.client.fetch_keyword(keyword, max_pages)

            all_jobs.extend(self.normalize(job) for job in raw_jobs)

        return all_jobs

    def normalize(self, raw_job):
        job = raw_job["MatchedObjectDescriptor"]

        return {
            "id": job["PositionID"],
            "title": job["PositionTitle"],
            "company": job["OrganizationName"],
            "location": job["PositionLocationDisplay"],
            "description": job.get("UserArea", {})
            .get("Details", {})
            .get("JobSummary", ""),
            "source": "USAJobs",
            "source_id": job["PositionID"],
            "date_posted": job.get("PublicationStartDate"),
            "raw": raw_job
        }