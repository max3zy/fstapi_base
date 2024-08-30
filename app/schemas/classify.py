from pydantic import BaseModel, Field


class ClassifyResponse(BaseModel):
    translation: str = Field(
        ...,
        description="translation",
    )