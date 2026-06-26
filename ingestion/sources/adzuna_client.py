# aduzna_client.py
import requests
from ingestion.config import ADZUNA_ID, ADZUNA_API_KEY, validate_config

BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search"

class AdzunaClient:
    def __init__(self):
        validate_config()

    def fetch_page(self, keyword: str, page: int = 1, results_per_page: int = 50):
        params = {
            "app_id": ADZUNA_ID,
            "app_key": ADZUNA_API_KEY,
            "what": keyword,
            "results_per_page": results_per_page
        }

        response = requests.get(f"{BASE_URL}/{page}", params=params, timeout=15)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(
                f"""
                Adzuna request failed

                Status: {response.status_code}

                Response:
                {response.text}
                """
            ) from e

        return response.json()
    
    def fetch_all(self, keyword: str, max_pages: int = 5):
        all_jobs = []

        for page in range(1, max_pages + 1):
            data = self.fetch_page(keyword, page=page)

            jobs = data.get("results", [])

            if not jobs:
                break

            all_jobs.extend(jobs)

        return all_jobs

    def fetch_keyword(self, keyword: str, max_pages : int = 5):
        return self.fetch_all(keyword, max_pages=max_pages)