
"""Leg configuration"""

from dataclasses import dataclass

@dataclass
class LegConfig:
    """Leg configuation"""

    coaxia_length: float = 0
    femur_length:  float = 0
    tibia_length:  float = 0
