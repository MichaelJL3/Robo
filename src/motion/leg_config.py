
from dataclasses import dataclass


from dataclasses import dataclass

@dataclass
class LegConfig(object):
    """Leg configuation"""

    coaxia_length: float = 0
    femur_length:  float = 0
    tibia_length:  float = 0
