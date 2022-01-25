
"""Forward kinematic tests based on graphical analysis"""

import unittest

from parameterized import parameterized

import numpy.testing as nptest

import arachnid.kinematics.graphical_kinematics as gkinematics

from robotics.body.leg_3dof import Leg3DOF
from robotics.typings.types import Vector3

class TestInverseKinematicGraphicalArachneSolver(unittest.TestCase):
    """Forward kinematic tests based on graphical analysis"""

    @parameterized.expand([
        [(97,      -77,     0     ), (90.0,  90.0, 90.0)],
        [(122.092, -64.54,  33.859), (74.5,  78.4, 101.599)],
        [(108.375, -64.54,  65.634), (58.8,  78.4, 101.599)],
        [(126.7,   -64.54, -0.442 ), (90.2,  78.4, 101.601)],
        [(66,       108.0,  0     ), (90.0,  0.0,  180.0 )],
        [(85.923,  -64.54, -93.114), (137.3, 78.4, 101.599)]
    ])
    def test_solve(self, dst: Vector3, expected: Vector3):
        """Test that solver copmutes forward position

        Args:
            dst (Vector3): the input destination
            expected (Vector3): the expected theta rotations output
        """
        config = __test_config__()

        pos = gkinematics.solve_inverse_kinematic(config, dst)

        self.assertEqual(len(expected), len(pos))
        nptest.assert_almost_equal(expected, pos, decimal = 3)

class TestForwardKinematicGraphicalArachneSolver(unittest.TestCase):
    """Forward kinematic tests based on graphical analysis"""

    @parameterized.expand([
        [(90.0,  90.0, 90.0), (97,      -77,     0     )],
        [(74.5,  78.4, 78.4), (122.092, -64.54,  33.859)],
        [(58.8,  78.4, 78.4), (108.375, -64.54,  65.634)],
        [(90.2,  78.4, 78.4), (126.7,   -64.54, -0.442 )],
        [(90.2,  0.0,  0.0 ), (66,       108.0, -0.23  )],
        [(137.3, 78.4, 78.4), (85.923,  -64.54, -93.114)]
    ])
    def test_solve(self, thetas: Vector3, expected: Vector3):
        """Test that solver copmutes forward position

        Args:
            thetas (Vector3): the input test theta rotations
            expected (Vector3): the expected position output
        """
        config = __test_config__()

        pos = gkinematics.solve_forward_kinematic(config, thetas)

        self.assertEqual(len(expected), len(pos))
        nptest.assert_almost_equal(expected, pos, decimal = 3)

def __test_config__() -> Leg3DOF:
    """Mock frame data

    Returns:
        Leg3DOF: mock config
    """
    return Leg3DOF(66.0, 31.0, 77.0)
