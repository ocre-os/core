from fastapi import FastAPI, HTTPException
from sqlalchemy import text

from app.core.config import get_settings
from app.core.database import engine
from app.modules.organizations.router import router as organizations_router

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

app.include_router(organizations_router, prefix="/api/v1")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as exc:
        raise HTTPException(status_code=503, detail="database_unavailable") from exc

    return {
        "status": "ok",
        "database": "ok",
        "environment": settings.env,
    }
