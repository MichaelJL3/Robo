
from functools import reduce
from typing import List

from ..frame import Frame
from ..transform import FrameTransform

class ForwardKinematicFrameSolver(object):
    """Forward kinematics frame solver class"""

    @staticmethod
    def solve(frames: List[Frame]):
        """fetch effector position based on frames theta rotations

        Args:
            frames (frames[]): array of frames

        Returns:
            Tuple[float, float, float]: The effector position
        """

        transforms = map(FrameTransform.apply_3d, frames)
        effector = reduce(lambda a, b: a.dot(b), transforms)

        return (effector[0][3], effector[2][3], effector[1][3])
