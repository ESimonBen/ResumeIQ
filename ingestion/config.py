# config.py
import os
from dotenv import load_dotenv

load_dotenv()

USAJOBS_API_KEY = os.getenv("USAJOBS_API_KEY")
USAJOBS_EMAIL = os.getenv("USAJOBS_EMAIL")
THEIRSTACK_API_KEY = os.getenv("THEIRSTACK_API_KEY")
ADZUNA_ID = os.getenv("ADZUNA_ID")
ADZUNA_API_KEY = os.getenv("ADZUNA_API_KEY")


def validate_config():
    if not USAJOBS_API_KEY or not USAJOBS_EMAIL:
        raise ValueError("Missing USAJobs API credentials in .env")

    if not THEIRSTACK_API_KEY:
        raise ValueError("Missing TheirStack API credentials in .env")

    if not ADZUNA_ID or not ADZUNA_API_KEY:
        raise ValueError("Missing Adzuna API credentials in .env")