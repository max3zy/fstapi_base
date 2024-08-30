from app.estimators.classifiers import ClassifierRuBert, TranslatorHlsnk
from app.utils.types import EstimatorIn, StrategyIn


class ClassifyService:
    def __init__(self, classifier: ClassifierRuBert):
        self.classifier = classifier

    def predict(self, estimator_in: EstimatorIn) -> StrategyIn:
        score = self.classifier.predict(query=estimator_in.query)
        if not estimator_in.is_use_score:
            score = 1.0 if score > estimator_in.threshold else 0.0
        return StrategyIn(query=estimator_in.query, classify_score=score)


class TranslateService:
    def __init__(self, translator: TranslatorHlsnk):
        self.translator = translator

    def predict(self, estimator_in: EstimatorIn):
        translation = self.translator.predict(query=estimator_in.query)
        return StrategyIn(
            query=estimator_in.query,
            translation=translation
        )