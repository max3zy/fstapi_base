from app.schemas.root import Root
from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=Root)
async def root() -> Root:
    response = Root()
    return response
