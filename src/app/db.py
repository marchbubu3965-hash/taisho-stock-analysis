from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from app.config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)

def get_db_status() -> bool:
    """Return True if DB connection ok."""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except SQLAlchemyError:
        return False
