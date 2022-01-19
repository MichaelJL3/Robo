
"""Gait generation for movements"""

from typing import Tuple
from .gait import Gait

class GaitRotational(Gait):
    """Gait class"""

    def __gait_provider__(self, index: int) -> Tuple[float, float, float]:
        """Generate the gait in terms of angle rotations

        Args:
            index (int): the step in the movement

        Returns:
            Tuple[float, float, float]: the rotations
        """
        if index == 0:
            return (90, 13, 13)
        if index == 1:
            return (140, 90, 90)

        theta_1 = -20 * index + 170
        theta_2 = theta_3 = 90

        return (theta_1, theta_2, theta_3)
