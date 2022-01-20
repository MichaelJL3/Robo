
"""Leg state"""

from dataclasses import dataclass
from typing import Tuple

from .leg_config import LegConfig

Position = Tuple[float, float, float]

@dataclass
class LegState:
    """Leg configuation"""

    config: LegConfig
    position: Position
    walking_id: int
    turning_id: int
