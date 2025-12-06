import os
from dotenv import load_dotenv

# Load .env file if exists
load_dotenv()

# Database URL (used by db.py)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/taisho_db"
)

# App settings
APP_NAME = "Taisho Stock Analysis API"
ENV = os.getenv("ENV", "development")
