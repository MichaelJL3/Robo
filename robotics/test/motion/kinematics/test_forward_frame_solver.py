
"""Forward kinematic tests based on references frames"""

import unittest

from parameterized import parameterized

import numpy.testing as nptest

from robotics.typings.types import Vector3
from robotics.motion.frame.frame import Frame
import robotics.motion.kinematics.forward_frame as fkinematics

class TestForwardFrameSolver(unittest.TestCase):
    """Forward kinematic tests based on references frames"""

    @parameterized.expand([
        [(90.0,  90.0, 90.0), (97,      -77,     0     )],
        [(74.5,  78.4, 78.4), (122.092, -64.54,  33.859)],
        [(58.8,  78.4, 78.4), (108.375, -64.54,  65.634)],
        [(90.2,  0.0,  0.0 ), (66,       108.0, -0.23  )],
        [(137.3, 78.4, 78.4), (85.923,  -64.54, -93.114)]
    ])
    def test_solve(self, thetas: Vector3, expected: Vector3):
        """Test that solver copmutes forward position

        Args:
            thetas (Vector3): the input test theta rotations
            expected (Vector3): the expected position output
        """
        frames = __test_frames__()

        # modify the frames by the new set of thetas
        for frame, theta in zip(frames, thetas):
            frame.theta -= theta

        pos = fkinematics.solve_forward_kinematic(frames)

        self.assertEqual(len(expected), len(pos))
        nptest.assert_almost_equal(expected, pos, decimal = 3)

def __test_frames__():
    """Mock frame data

    Returns:
        List[Frame]: mock frames
    """
    return [
        Frame(rho = 66.0, alpha = 90.0, theta = 90.0),
        Frame(rho = 31.0, theta = 90.0),
        Frame(rho = 77.0)
    ]
