
"""Part"""

from dataclasses import dataclass
from typing import Generic

from robotics.typings.types import Vector3, Config

@dataclass
class Part:
    """Part state/configuration"""

    config: Generic[Config]
    position: Vector3
    name: str
