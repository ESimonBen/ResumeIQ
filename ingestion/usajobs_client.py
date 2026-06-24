# usajobs_client.py
import requests
from ingestion.config import USAJOBS_API_KEY, USAJOBS_EMAIL, validate_config

BASE_URL = "https://data.usajobs.gov/api/search"

class USAJobsClient:
    def __init__(self):
        validate_config()

        self.headers = {
            "Host": "data.usajobs.gov",
            "User-Agent": USAJOBS_EMAIL,
            "Authorization-Key": USAJOBS_API_KEY,
        }

    def fetch_page(self, keyword: str, page: int = 1, results_per_page: int = 100):
        params = {
            "Keyword": keyword,
            "ResultsPerPage": results_per_page,
            "Page": page,
        }

        response = requests.get(
            BASE_URL,
            headers=self.headers,
            params=params,
            timeout=15,
        )

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(
                f"USAJobs API request failed | "
                f"keyword={keyword} page={page} status={response.status_code}"
            ) from e

        return response.json()

    def fetch_all(self, keyword: str, max_pages: int = 5):
        all_jobs = []

        for page in range(1, max_pages + 1):
            data = self.fetch_page(keyword, page=page)

            jobs = data.get("SearchResult", {}).get("SearchResultItems", [])

            if not jobs:
                break

            all_jobs.extend(jobs)

        return all_jobs

    def fetch_keyword(self, keyword: str, max_pages : int = 5):
        return self.fetch_all(keyword, max_pages=max_pages)