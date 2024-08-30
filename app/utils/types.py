from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ClassifyRequest:
    query: str


@dataclass
class EstimatorIn:
    query: str
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class StrategyIn:
    query: str
    translation: Optional[str] = 'lol'
    debug_info: Optional[Dict[str, Any]] = None


@dataclass
class StrategyOut:
    query: str
    classify_score: Optional[float] = 0.1
    translation: Optional[str] = 'lol'
    debug_info: Optional[Dict[str, Any]] = None
