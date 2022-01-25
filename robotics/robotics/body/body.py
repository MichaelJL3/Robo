
"""Body"""

from dataclasses import dataclass
from typing import List

from robotics.body.part import Part

@dataclass
class Body:
    """Body state/configuration"""

    parts: List[Part]
