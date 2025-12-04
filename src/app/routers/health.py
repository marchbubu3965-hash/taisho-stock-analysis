from fastapi import APIRouter
from app.db import get_db_status

router = APIRouter()

@router.get("/health")
def health_check():
    db_ok = get_db_status()
    return {
        "status": "ok",
        "database": "connected" if db_ok else "failed"
    }
