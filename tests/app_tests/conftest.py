import pandas as pd
import pytest
from app.config import settings
from app.estimators.classifiers import ClassifierRuBert
from app.estimators.loaders import OnnxLoader


@pytest.fixture()
def requests_classify_critical():
    df = pd.read_csv(
        "./tests/resources/requests_classify_critical.csv", sep=";"
    )
    return df


@pytest.fixture()
def requests_classify_all():
    df = pd.read_csv("./tests/resources/requests_classify_all.csv", sep=";")
    return df


@pytest.fixture()
def onnx_loader():
    loader = OnnxLoader(
        path_to_models=settings.path_to_models,
        classifier_model=settings.classifier_onnx_model,
    )
    return loader


@pytest.fixture()
def classifier_ru_bert(onnx_loader):
    classifier = ClassifierRuBert(loader=onnx_loader)
    return classifier


@pytest.fixture()
def empty_query():
    return ""


@pytest.fixture()
def big_query():
    query = """
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    Здесь должен быть какой-то большой бредовый текст
    """
    return query


@pytest.fixture()
def stupid_query():
    return "Как сварить пельмени"
