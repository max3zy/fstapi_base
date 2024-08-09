from pydantic import BaseModel, Field


class ClassifyResponse(BaseModel):
    classify_score: float = Field(
        ...,
        description="Все варианты для дополнения текста пользователя",
    )
