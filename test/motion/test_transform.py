
"""Transformation tests"""

import unittest
import numpy.testing as nptest

from parameterized import parameterized

from src.motion.frame import Frame
from src.motion.transform import frame_3d_transform_matrix

class TestFrameTrasnform(unittest.TestCase):
    """Transformation tests"""

    @parameterized.expand([
        [Frame(0,  0, 90, 66), [
            [1, 0,  0, 66],
            [0, 0, -1, 0 ],
            [0, 1,  0, 0 ],
            [0, 0,  0, 1 ]
        ]],
        [Frame(0,  0, 0,  31), [
            [1, 0, 0, 31],
            [0, 1, 0, 0 ],
            [0, 0, 1, 0 ],
            [0, 0, 0, 1 ]
        ]],
        [Frame(90, 0, 0,  77), [
            [0, -1, 0, 0 ],
            [1,  0, 0, 77],
            [0,  0, 1, 0 ],
            [0,  0, 0, 1 ]
        ]],
        [Frame(45, 0, 0,  31), [
            [0.707, -0.707, 0, 21.92],
            [0.707,  0.707, 0, 21.92],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]]
    ])
    def test_frame_transform(self, frame: Frame, expected):
        """Test frame transforms

        Args:
            frame (Frame): the reference frame
            expected ([float]): expected transform matrix
        """
        transform = frame_3d_transform_matrix(frame)
        self.assertEqual(len(expected), len(transform))
        nptest.assert_array_almost_equal(transform, expected, decimal = 3)
