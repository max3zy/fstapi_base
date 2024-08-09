from abc import ABC, abstractmethod

from app.schemas.classify import ClassifyResponse
from app.utils.types import StrategyIn, StrategyOut


class AbstractStrategyPrediction(ABC):
    @abstractmethod
    def process(self, strategy_in: StrategyIn) -> StrategyOut:
        pass


class TrivialStrategy(AbstractStrategyPrediction):
    def process(self, strategy_in: StrategyIn) -> StrategyOut:
        return StrategyOut(
            query=strategy_in.query,
            classify_score=strategy_in.classify_score,
        )


def create_answer(strategy_output: StrategyOut) -> ClassifyResponse:
    return ClassifyResponse(classify_score=strategy_output.classify_score)
