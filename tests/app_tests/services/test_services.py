import pytest
from app.config import settings
from app.services.classify_service import ClassifyService
from app.utils.types import EstimatorIn, StrategyIn


@pytest.fixture(
    scope="module",
    params=[
        "classifier_ru_bert",
    ],
)
def test_classify_service_empty_query(classifier, empty_query):
    service = ClassifyService(classifier=classifier)
    estimator_in = EstimatorIn(
        query=empty_query, is_use_score=False, threshold=settings.THRESHOLD
    )
    strategy_in = service.predict(estimator_in)
    assert isinstance(strategy_in, StrategyIn)
    assert strategy_in.classify_score == 0


@pytest.fixture(
    scope="module",
    params=[
        "classifier_ru_bert",
    ],
)
def test_classify_service_big_query(classifier, big_query):
    service = ClassifyService(classifier=classifier)
    estimator_in = EstimatorIn(
        query=big_query, is_use_score=False, threshold=settings.THRESHOLD
    )
    strategy_in = service.predict(estimator_in)
    assert isinstance(strategy_in, StrategyIn)
    assert strategy_in.classify_score == 0


@pytest.fixture(
    scope="module",
    params=[
        "classifier_ru_bert",
    ],
)
def test_classify_service_stupid_query(classifier, stupid_query):
    service = ClassifyService(classifier=classifier)
    estimator_in = EstimatorIn(
        query=stupid_query, is_use_score=False, threshold=settings.THRESHOLD
    )
    strategy_in = service.predict(estimator_in)
    assert isinstance(strategy_in, StrategyIn)
    assert strategy_in.classify_score == 0
