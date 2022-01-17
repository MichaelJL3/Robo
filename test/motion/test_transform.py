
import unittest
import numpy.testing as nptest

from parameterized import parameterized

from src.motion.frame import Frame
from src.motion.transform import FrameTransform

class TestFrameTrasnform(unittest.TestCase):
    @parameterized.expand([
        [66, 90, 0, 0 , [[1, 0, 0, 66], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]],
        [31, 0,  0, 0 , [[1, 0, 0, 31], [0, 1, 0,  0], [0, 0, 1, 0], [0, 0, 0, 1]]],
        [77, 0,  0, 90, [[0, -1, 0, 0], [1, 0, 0, 77], [0, 0, 1, 0], [0, 0, 0, 1]]],
        [31, 0,  0, 45, [[0.707, -0.707, 0, 21.92], [0.707, 0.707, 0, 21.92], [0, 0, 1, 0], [0, 0, 0, 1]]]
    ])
    def test_frame_transform(self, rho, alpha, delta, theta, expected):
        """Test frame transforms

        Args:
            rho (float): rho
            alpha (float): alpha
            delta (float): delta
            theta (float): theta
            expected ([float]): expected transform matrix
        """

        frame = Frame(theta, delta, alpha, rho)
        transform = FrameTransform.apply_3d(frame)

        nptest.assert_array_almost_equal(transform, expected, decimal = 3)
