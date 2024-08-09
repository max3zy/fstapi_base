from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ClassifyRequest:
    query: str
    is_use_score: bool
    threshold: float


@dataclass
class EstimatorIn:
    query: str
    is_use_score: bool
    threshold: float
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class StrategyIn:
    query: str
    classify_score: float
    debug_info: Optional[Dict[str, Any]] = None


@dataclass
class StrategyOut:
    query: str
    classify_score: float
    debug_info: Optional[Dict[str, Any]] = None
