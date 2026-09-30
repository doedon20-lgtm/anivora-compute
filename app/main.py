from fastapi import FastAPI

from app.config import Config
from app.api.routes import router


app = FastAPI(
    title=Config.APP_NAME,
    version=Config.VERSION,
    description=(
        "AniVora GPU and compute "
        "infrastructure."
    )
)


@app.get("/")
def root():

    return {
        "name": Config.APP_NAME,
        "status": "online",
        "version": Config.VERSION
    }


@app.get("/health")
def health():

    return {
        "success": True,
        "service": Config.APP_NAME,
        "status": "healthy"
    }


app.include_router(router)
