import os
from sqlalchemy import create_engine

def get_engine():
    db_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/stock_db")
    engine = create_engine(db_url, echo=False)
    return engine

