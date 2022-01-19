
"""Gait generation for movements"""

from typing import Tuple

from .gait import Gait

class GaitPositional(Gait):
    """Gait class"""

    _gait_as_dst = [
        (106.73,  99.41,   0.00),
        ( 62.35, -77.00,  74.31),
        ( 74.31, -77.00, -62.35),
        ( 91.15, -77.00, -33.18),
        ( 97.00, -77.00,   0.00),
        ( 91.15, -77.00,  33.18),
        ( 74.31, -77.00,  62.35),
        ( 48.50, -77.00,  84.00)
    ]

    def __gait_provider__(self, index: int) -> Tuple[float, float, float]:
        """Generate the gait in terms of end effector position

        Args:
            index (int): the step in the movement

        Returns:
            Tuple[float, float, float]: the position
        """
        return self._gait_as_dst[index]
