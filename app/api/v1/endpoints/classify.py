from app.api.conainers import AppContainer
from app.config import settings
from app.preprocesses.preprocesses import preprocess
from app.schemas.classify import ClassifyResponse
from app.services.classify_service import ClassifyService, TranslateService
from app.strategies.strategies import TrivialStrategy, create_answer
from app.utils.types import ClassifyRequest
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get(
    "/translate",
    response_model=ClassifyResponse,
    response_model_exclude_none=True,
)
@inject
async def translate(
    query: str, # russian plain text
    service: TranslateService = Depends(Provide[AppContainer.service_base]),
    strategy: TrivialStrategy = Depends(
        Provide[AppContainer.trivial_strategy]
    ),
) -> ClassifyResponse:
    request = ClassifyRequest(query=query)
    estimator_input = preprocess(request=request)
    estimator_output = service.predict(estimator_in=estimator_input)
    strategy_output = strategy.process(strategy_in=estimator_output)
    return create_answer(strategy_output=strategy_output)
