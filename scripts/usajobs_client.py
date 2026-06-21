# usajobs_client.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("USAJOBS_API_KEY")
EMAIL = os.getenv("USAJOBS_EMAIL")

BASE_URL = "https://data.usajobs.gov/api/search"

def fetch_jobs(keyword="software", results_per_page=10):
    headers = {
        "Host" : "data.usajobs.gov",
        "User_Agent": EMAIL,
        "Authorization-Key": API_KEY
    }

    params = {
        "Keyword" : keyword,
        "ResultsPerPage" : results_per_page
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    response.raise_for_status()

    return response.json()