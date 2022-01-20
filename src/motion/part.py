
"""Part"""

from dataclasses import dataclass
from typing import Generic, Tuple, TypeVar

Type = TypeVar('Type')
Position = Tuple[float, float, float]

@dataclass
class Part:
    """Part state/configuration"""

    config: Generic[Type]
    position: Position
    walking_id: int
    turning_id: int
