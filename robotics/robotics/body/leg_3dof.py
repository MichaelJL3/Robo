
"""3 degrees of freedom leg configuration"""

from dataclasses import dataclass

@dataclass
class Leg3DOF:
    """3 degrees of freedom leg configuation"""

    coaxia_length: float = 0
    femur_length:  float = 0
    tibia_length:  float = 0
