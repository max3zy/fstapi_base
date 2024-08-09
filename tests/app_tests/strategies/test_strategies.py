from abc import ABC

from app.schemas.classify import ClassifyResponse
from app.strategies.strategies import (
    AbstractStrategyPrediction,
    TrivialStrategy,
    create_answer,
)
from app.utils.types import StrategyIn, StrategyOut


def test_abstract_strategy():
    assert issubclass(AbstractStrategyPrediction, ABC)
    assert "process" in AbstractStrategyPrediction.__abstractmethods__


def test_trivial_strategy():
    strategy_in = StrategyIn(query="Some query", classify_score=0.12)

    trivial_strategy = TrivialStrategy()
    strategy_out = trivial_strategy.process(strategy_in)
    assert isinstance(strategy_out, StrategyOut)


def test_create_answer():
    strategy_out = StrategyOut(query="Some query", classify_score=0.12)
    response = create_answer(strategy_out)
    assert isinstance(response, ClassifyResponse)
