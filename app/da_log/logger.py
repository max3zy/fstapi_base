from typing import Any, Dict

from app.config import settings
from yaml import safe_load


def get_log_config() -> Dict[str, Any]:
    with open(settings.LOGGER_CONFIG, "r", encoding=settings.ENCODING) as cfg:
        return safe_load(cfg)
