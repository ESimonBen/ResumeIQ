# paths.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

DB_PATH = RAW_DIR / "resumeiq.db"
DATASET_PATH = PROCESSED_DIR / "dataset.csv"