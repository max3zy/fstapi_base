import os

from onnxruntime import (
    GraphOptimizationLevel,
    InferenceSession,
    SessionOptions,
    get_all_providers,
)
from transformers import BertTokenizerFast


class OnnxLoader:
    def __init__(
        self,
        path_to_models: str,
        classifier_model: str,
        provider: str = "CPUExecutionProvider",
        core_count: int = 1,
    ):
        self.provider = provider
        self.core_count = core_count
        self.tokenizer = self.load_tokenizer(path_to_models)
        self.session = self.load_model(path_to_models, classifier_model)
        self.tokenizer_inputs = {inp.name for inp in self.session.get_inputs()}
        self.tokenizer_outputs = [
            out.name for out in self.session.get_outputs()
        ]

    def load_model(
        self, path_to_models: str, classifier_model: str
    ) -> InferenceSession:
        assert (
            self.provider in get_all_providers()
        ), f"provider {self.provider} not found, {get_all_providers()}"
        model_path = os.path.join(path_to_models, classifier_model)
        options = SessionOptions()
        options.intra_op_num_threads = self.core_count
        options.graph_optimization_level = (
            GraphOptimizationLevel.ORT_ENABLE_ALL
        )
        session = InferenceSession(
            model_path, options, providers=[self.provider]
        )

        session.disable_fallback()
        return session

    @staticmethod
    def load_tokenizer(path_to_models: str) -> BertTokenizerFast:
        tokenizer_path = os.path.join(path_to_models, "tokenizer")
        tokenizer = BertTokenizerFast.from_pretrained(
            tokenizer_path, local_files_only=True
        )
        return tokenizer
