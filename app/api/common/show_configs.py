from app.config import settings
from fastapi import APIRouter

router = APIRouter()


@router.get("/get_configs")
async def get_configs():
    return settings
