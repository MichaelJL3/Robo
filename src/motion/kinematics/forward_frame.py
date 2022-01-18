
"""Forward kinematics through reference frames"""

from functools import reduce
from typing import List

from ..frame import Frame
from ..transform import frame_3d_transform_matrix

class ForwardKinematicFrame:
    """Forward kinematics frame solver class"""

    @staticmethod
    def solve(frames: List[Frame]):
        """fetch effector position based on frames theta rotations

        Args:
            frames (frames[]): array of frames

        Returns:
            Tuple[float, float, float]: The effector position
        """

        transforms = map(frame_3d_transform_matrix, frames)
        effector = reduce(lambda a, b: a.dot(b), transforms)

        return (effector[0][3], effector[2][3], effector[1][3])
