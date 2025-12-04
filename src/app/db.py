from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from app.config import DATABASE_URL

def get_db_status():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return True
    except SQLAlchemyError:
        return False
