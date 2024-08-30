import numpy as np
from app.estimators.loaders import OnnxLoader, TrivialLoader


class TranslatorHlsnk:
    def __init__(self, loader: TrivialLoader):
        self.tokenizer = loader.tokenizer
        self.model = loader.model

    def predict(self, query: str) -> str:
        input_ids = self.tokenizer.encode(query, return_tensors="pt")
        outputs = self.model.generate(input_ids)
        decoded_answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return decoded_answer


class ClassifierRuBert:
    def __init__(self, loader: OnnxLoader):
        self.session = loader.session
        self.tokenizer = loader.tokenizer
        self.tokenizer_outputs = loader.tokenizer_outputs
        self.tokenizer_inputs = loader.tokenizer_inputs

    def predict(self, query: str) -> float:
        encoded_input = self.tokenizer(
            query, padding=True, truncation=True, return_tensors="np"
        )
        logits = self.session.run(
            self.tokenizer_outputs,
            {
                key: val
                for key, val in encoded_input.items()
                if key in self.tokenizer_inputs
            },
        )[0].flatten()
        score = float(self.softmax(logits)[1])
        return score

    @staticmethod
    def softmax(logits: np.ndarray) -> np.ndarray:
        nominator = np.exp(logits - np.max(logits))
        divider = np.sum(np.exp(logits - np.max(logits)))
        return nominator / divider
