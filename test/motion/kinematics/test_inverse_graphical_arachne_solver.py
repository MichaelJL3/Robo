
"""Forward kinematic tests based on graphical analysis"""

import unittest

from typing import Tuple
from parameterized import parameterized

import numpy.testing as nptest

from src.motion.leg_config import LegConfig
import src.motion.kinematics.inverse_graphical_arachne as ikg
from test.motion.kinematics.mock_config import mock_leg_config

class TestInverseKinematicGraphicalArachneSolver(unittest.TestCase):
    """Forward kinematic tests based on graphical analysis"""

    @parameterized.expand([
        [(97,      -77,     0     ), (90.0,  90.0, 90.0)],
        [(122.092, -64.54,  33.859), (74.5,  78.4, 78.4)],
        [(108.375, -64.54,  65.634), (58.8,  78.4, 78.4)],
        [(126.7,   -64.54, -0.442 ), (90.2,  78.4, 78.4)],
        [(66,       108.0,  0     ), (90.0,  0.0,  0.0 )],
        [(85.923,  -64.54, -93.114), (137.3, 78.4, 78.4)]
    ])
    def test_solve(self, dst: Tuple[float, float, float], expected: Tuple[float, float, float]):
        """Test that solver copmutes forward position

        Args:
            dst (Tuple[float, float, float]): the input destination
            expected (Tuple[float, float, float]): the expected theta rotations output
        """
        config = mock_leg_config()

        pos = ikg.solve_inverse_kinematic(config, dst)

        nptest.assert_almost_equal(expected, pos, decimal = 3)
