
"""Part"""

from dataclasses import dataclass
from typing import Generic

from robotics.typings.types import Position, Config

@dataclass
class Part:
    """Part state/configuration"""

    config: Generic[Config]
    position: Position
    walking_id: int
    turning_id: int
