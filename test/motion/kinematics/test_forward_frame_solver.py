
import unittest
import numpy.testing as nptest

from typing import Tuple
from parameterized import parameterized

from src.motion.frame import Frame
from src.motion.kinematics.forward_frame_solver import ForwardKinematicFrameSolver

class TestForwardFrameSolver(unittest.TestCase):
    @parameterized.expand([
        [(90.0,  90.0, 90.0), (97, -77, 0)],
        [(74.5,  78.4, 78.4), (122.092, -64.54, 33.859)],
        [(58.8,  78.4, 78.4), (108.375, -64.54, 65.634)],
        [(90.2,  78.4, 78.4), (126.7, -64.54, -0.442)],
        [(90.2,  0.0,  0.0 ), (66, 108.0, -0.23)],
        [(137.3, 78.4, 78.4), (85.923, -64.54, -93.114)]
    ])
    def test_solve(self, thetas: Tuple[float, float, float], expected: Tuple[float, float, float]):
        """Test that solver copmutes forward position

        Args:
            thetas (Tuple[float, float, float]): the input test theta rotations
            expected (Tuple[float, float, float]): the expected position output
        """
        frames = self.__test_frames__()
        
        # modify the frames by the new set of thetas
        for frame, theta in zip(frames, thetas):
            frame.theta -= theta

        pos = ForwardKinematicFrameSolver.solve(frames)

        nptest.assert_almost_equal(expected, pos, decimal = 3)

    def __test_frames__(self):
        """Mock frame data

        Returns:
            List[Frame]: mock frames
        """
        return [
            Frame(rho = 66.0, alpha = 90.0, theta = 90.0),
            Frame(rho = 31.0, theta = 90.0),
            Frame(rho = 77.0)
        ]