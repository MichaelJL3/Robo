
"""Gait generation for movements"""

from arachnid.gait.gait import Gait

from robotics.math.reflections import quadrant_2_x
from robotics.typings.types import Vector3

class GaitRotational(Gait):
    """Rotational gait"""

    def __gait_provider__(self, index: int, reverse: bool = False) -> Vector3:
        """Generate the gait in terms of angle rotations

        Args:
            index (int): the step in the movement
            reverse (bool, optional): whether to reverse the direction. Defaults to false.

        Returns:
            Vector3: the rotations
        """
        if index == 0:
            return (90, 13, 13)
        if index == 1:
            move = (140, 90, 90)
            return quadrant_2_x(move) if reverse else move

        theta_1 = -20 * index + 170
        theta_2 = theta_3 = 90

        move = (theta_1, theta_2, theta_3)
        return quadrant_2_x(move) if reverse else move
