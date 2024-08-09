from app.api.conainers import AppContainer
from app.config import settings
from app.preprocesses.preprocesses import preprocess
from app.schemas.classify import ClassifyResponse
from app.services.classify_service import ClassifyService
from app.strategies.strategies import TrivialStrategy, create_answer
from app.utils.types import ClassifyRequest
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get(
    "/classify",
    response_model=ClassifyResponse,
    response_model_exclude_none=True,
)
@inject
async def classify(
    query: str,
    is_use_score: bool = False,
    threshold: float = settings.THRESHOLD,
    # service: ClassifyService = Depends(Provide[AppContainer.service_ru_bert]),
    strategy: TrivialStrategy = Depends(
        Provide[AppContainer.trivial_strategy]
    ),
) -> ClassifyResponse:
    """
    Workflow
       1.preprocess
       2.predictor
       3.strategy post-process
       4.create answer
    :param query: запрос пользователя на дополнение
    :param is_use_score: выводить вероятность или метку класса
    :param threshold: порог срабатывания классификатора
    :param service:
    :param strategy:
    :return:
    """
    request = ClassifyRequest(
        query=query, is_use_score=is_use_score, threshold=threshold
    )
    estimator_input = preprocess(request=request)
    # estimator_output = service.predict(estimator_in=estimator_input)
    strategy_output = strategy.process(strategy_in=estimator_output)
    return create_answer(strategy_output=strategy_output)
