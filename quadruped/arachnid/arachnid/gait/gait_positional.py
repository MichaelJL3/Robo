
"""Gait generation for movements"""

from arachnid.gait.gait import Gait

from robotics.math.reflections import x_axis_3d
from robotics.typings.types import Vector3

class GaitPositional(Gait):
    """Positional gait"""

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

    def __gait_provider__(self, index: int, reverse: bool = False) -> Vector3:
        """Provide the gait in terms of physical location relative to the part base

        Args:
            index (int): the passed in index
            reverse (bool, optional): whether to reverse the direction. Defaults to false.

        Returns:
            Vector3: the gait position
        """
        move = self._gait_as_dst[index]
        return x_axis_3d(move) if reverse else move
