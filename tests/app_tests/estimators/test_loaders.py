from app.config import settings
from app.estimators.loaders import OnnxLoader


def test_onnx_loader(onnx_loader):
    assert isinstance(onnx_loader, OnnxLoader)
