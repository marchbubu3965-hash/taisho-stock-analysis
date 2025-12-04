from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI(title="Taisho Stock Analysis API")

app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "Stock Analysis API Running"}
