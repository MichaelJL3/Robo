
"""Forward kinematics through reference frames"""

from functools import reduce
from typing import List

from robotics.typings.types import Position
from robotics.motion.frame.frame import Frame
from robotics.motion.frame.transform import frame_3d_transform_matrix

def solve_forward_kinematic(frames: List[Frame]) -> Position:
    """fetch effector position based on frames theta rotations

    Args:
        frames (List[frames]): array of frames

    Returns:
        Position: The effector position
    """
    transforms = map(frame_3d_transform_matrix, frames)
    effector = reduce(lambda a, b: a.dot(b), transforms)

    return (effector[0][3], effector[2][3], effector[1][3])
