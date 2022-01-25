
"""Smoothing functions"""

from typing import List
from robotics.typings.types import Vector3, Matrix2

class Smoothing:
    """Smoothing class"""

    _pre_defined_arc = [.02, .05, .10, .25, .50, .75, .90, .95, .98, 1]

    def __init__(self, motion: List[float] = None):
        """create a distance smoothing function

        Args:
            motion (List[float], optional): the smoothing distribution. Defaults to None.
        """
        self._motion = motion if motion else self._pre_defined_arc

    def __call__(self, current_pos: Vector3, new_pos: Vector3) -> Matrix2:
        """Smoothen the rotation by splitting it into smaller parts

        Args:
            current_pos (Vector3): the current position
            new_pos (Vector3): the destination position

        Returns:
            Matrix2: the split moves between current and destination
        """
        return self.smooth(current_pos, new_pos)

    @property
    def motion(self) -> List[float]:
        """Get the smoothing motion

        Returns:
            List[float]: the smoothing motion
        """
        return self._motion

    def smooth(self, current_pos: Vector3, new_pos: Vector3) -> Matrix2:
        """Smoothen the rotation by splitting it into smaller parts

        Args:
            current_pos (Vector3): the current position
            new_pos (Vector3): the destination position

        Returns:
            Matrix2D: the split moves between current and destination
        """
        moves = []

        c_x, c_y, c_z = current_pos
        n_x, n_y, n_z = new_pos

        for pct in self._motion:
            move_a = c_x + (n_x - c_x) * pct
            move_b = c_y + (n_y - c_y) * pct
            move_c = c_z + (n_z - c_z) * pct
            moves.append((move_a, move_b, move_c))

        return moves
