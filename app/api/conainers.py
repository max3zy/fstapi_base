from app.config import settings
from app.estimators.classifiers import ClassifierRuBert, OnnxLoader
from app.services.classify_service import ClassifyService
from app.strategies.strategies import TrivialStrategy
from dependency_injector import containers, providers


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_dict(
        {
            "path_to_models": settings.PATH_TO_MODELS,
            "classifier_onnx_model": settings.CLASSIFIER_ONNX_MODEL,
        }
    )

    onnx_loader = providers.Singleton(
        OnnxLoader,
        path_to_models=config.path_to_models,
        classifier_model=config.classifier_onnx_model,
    )

    # classifier_ru_bert = providers.Singleton(
    #     ClassifierRuBert,
    #     loader=onnx_loader,
    # )
    #
    # service_ru_bert = providers.Singleton(
    #     ClassifyService,
    #     classifier=classifier_ru_bert,
    # )

    trivial_strategy = providers.Singleton(TrivialStrategy)
