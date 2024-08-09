from app.estimators.classifiers import ClassifierRuBert


def test_classifier_ru_bert(classifier_ru_bert):
    score = classifier_ru_bert.predict(query="Some query")
    assert isinstance(classifier_ru_bert, ClassifierRuBert)
    assert isinstance(score, float)
