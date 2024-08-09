from app.config import settings
from pydantic import BaseModel, Field


class HelloWorld(BaseModel):
    message: str = Field(
        "Hello world!",
        description="Приветственное сообщение от сервера",
        example=f"fastapi test project v {settings.SERVICE_VERSION}",
    )
