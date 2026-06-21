# config.py
import os
from dotenv import load_dotenv

load_dotenv()

USAJOBS_API_KEY = os.getenv("USAJOBS_API_KEY")
USAJOBS_EMAIL = os.getenv("USAJOBS_EMAIL")

def validate_config():
    if not USAJOBS_API_KEY or not USAJOBS_EMAIL:
        raise ValueError("Missing USAJobs API credentials in .env")