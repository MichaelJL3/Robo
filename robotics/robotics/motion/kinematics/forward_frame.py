
"""Forward kinematics through reference frames"""

from functools import reduce
from typing import List

from robotics.typings.types import Vector3
from robotics.motion.frame.frame import Frame
from robotics.motion.frame.transform import frame_3d_transform_matrix

def solve_forward_kinematic(frames: List[Frame]) -> Vector3:
    """fetch effector position based on frames theta rotations

    Args:
        frames (List[frames]): array of frames

    Returns:
        Vector3: The effector position
    """
    transforms = map(frame_3d_transform_matrix, frames)
    effector = reduce(lambda a, b: a.dot(b), transforms)

    return (effector[0][3], effector[2][3], effector[1][3])
