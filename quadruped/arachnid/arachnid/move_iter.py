
"""move iterator"""

from typing import Tuple

from robotics.typings.types import Matrix3

def move_iter(moves: Matrix3) -> Tuple[int, float]:
    """Create an iterator over the 3d matrix of smoothed motions among all parts

    Args:
        moves (Matrix3): the input matrix

    Yields:
        Tuple[int, float]: the tag of servo to the rotation
    """
    legs, motions, parts_per_leg = moves.shape

    for motion in range(motions):
        for part in range(parts_per_leg):
            for leg in range(legs):
                yield (leg * parts_per_leg + part, moves[leg, motion, part])
    