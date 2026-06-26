# theirstack_client.py
import requests
from ingestion.config import THEIRSTACK_API_KEY, validate_config

BASE_URL = "https://api.theirstack.com/v1/jobs/search"

class TheirStackClient:
    def __init__(self):
        validate_config()

        self.headers = {
            "Authorization": f"Bearer {THEIRSTACK_API_KEY}",
            "Content-Type": "application/json"
        }

    def fetch_page(self, keyword: str, page: int = 1, limit: int = 25):
        payload = {
            "job_title_or": [keyword],
            "posted_at_max_age_days": 30,
            "limit": limit,
            "page": page
        }

        response = requests.post(BASE_URL, json=payload, headers=self.headers, timeout=15)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(
                f"""
                TheirStack request failed
                
                Status: {response.status_code}
                
                Response:
                {response.text}
                """
            ) from e

        return response.json()

    def fetch_all(self, keyword: str, max_pages: int = 5):
        all_jobs = []

        for page in range(max_pages):
            data = self.fetch_page(keyword, page=page)

            jobs = data.get("data", [])

            if not jobs:
                break

            all_jobs.extend(jobs)

        return all_jobs

    def fetch_keyword(self, keyword: str, max_pages: int = 5):
        return self.fetch_all(keyword, max_pages=max_pages)