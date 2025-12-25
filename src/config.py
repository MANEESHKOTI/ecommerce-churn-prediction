import os
from pathlib import Path

# Project Root (calculated dynamically)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Model Directories
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Files
RAW_DATA_FILE = RAW_DATA_DIR / "online_retail.csv"
CLEANED_DATA_FILE = PROCESSED_DATA_DIR / "cleaned_transactions.csv"
SUBMISSION_FILE = PROJECT_ROOT / "submission.json"

# Create directories if they don't exist
for path in [RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, LOGS_DIR, FIGURES_DIR]:
    path.mkdir(parents=True, exist_ok=True)

# Random Seed for Reproducibility
RANDOM_STATE = 42