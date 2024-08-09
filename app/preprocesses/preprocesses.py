from app.utils.types import ClassifyRequest, EstimatorIn
from dictionary_lib.preprocess import text_cleanup_preprocessor


def preprocess(request: ClassifyRequest) -> EstimatorIn:
    cleanup_text = text_cleanup_preprocessor(request.query)
    return EstimatorIn(
        query=cleanup_text,
        is_use_score=request.is_use_score,
        threshold=request.threshold,
    )
