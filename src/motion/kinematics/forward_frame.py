
"""Forward kinematics through reference frames"""

from functools import reduce
from typing import List

from motion.frame import Frame
from motion.transform import frame_3d_transform_matrix

def solve_forward_kinematic(frames: List[Frame]):
    """fetch effector position based on frames theta rotations

    Args:
        frames (frames[]): array of frames

    Returns:
        Tuple[float, float, float]: The effector position
    """

    transforms = map(frame_3d_transform_matrix, frames)
    effector = reduce(lambda a, b: a.dot(b), transforms)

    return (effector[0][3], effector[2][3], effector[1][3])
