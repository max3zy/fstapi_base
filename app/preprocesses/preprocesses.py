from app.utils.preprocessors import text_cleanup_preprocessor
from app.utils.types import ClassifyRequest, EstimatorIn


def preprocess(request: ClassifyRequest) -> EstimatorIn:
    cleanup_text = text_cleanup_preprocessor(request.query)
    return EstimatorIn(
        query=cleanup_text
    )
