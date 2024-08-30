from app.config import settings, MODEL_PARAMS
from app.estimators.classifiers import ClassifierRuBert, OnnxLoader, TranslatorHlsnk
from app.estimators.loaders import TrivialLoader
from app.services.classify_service import ClassifyService, TranslateService
from app.strategies.strategies import TrivialStrategy
from dependency_injector import containers, providers


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    # config.from_dict(
    #     {
    #         "path_to_models": settings.PATH_TO_MODELS,
    #         "classifier_onnx_model": settings.CLASSIFIER_ONNX_MODEL,
    #     }
    # )
    config.from_dict(
        {
            "path_to_model": settings.TRANSLATOR.PATH_TO_MODEL,
            "path_to_tokenizer": settings.TRANSLATOR.PATH_TO_TOKENIZER,
        }
    )
    # config.from_dict(MODEL_PARAMS)

    # onnx_loader = providers.Singleton(
    #     OnnxLoader,
    #     path_to_models=config.path_to_models,
    #     classifier_model=config.classifier_onnx_model,
    # )

    trivial_loader = providers.Singleton(
        TrivialLoader,
        path_to_tokenizer=config.path_to_tokenizer,
        path_to_model=config.path_to_model
    )

    translator_base = providers.Singleton(
        TranslatorHlsnk,
        loader=trivial_loader,
    )

    service_base = providers.Singleton(
        TranslateService,
        translator=translator_base,
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
