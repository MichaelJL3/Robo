
import unittest

from typing import Tuple
from parameterized import parameterized

import numpy.testing as nptest

from src.motion.leg_config import LegConfig
from src.motion.kinematics.forward_graphical_arachne_solver import ForwardKinematicGraphicalArachneSolver

class TestForwardKinematicGraphicalArachneSolver(unittest.TestCase):
    @parameterized.expand([
        [(90.0,  90.0, 90.0), (97,      -77,     0     )],
        [(74.5,  78.4, 78.4), (122.092, -64.54,  33.859)],
        [(58.8,  78.4, 78.4), (108.375, -64.54,  65.634)],
        [(90.2,  78.4, 78.4), (126.7,   -64.54, -0.442 )],
        [(90.2,  0.0,  0.0 ), (66,       108.0, -0.23  )],
        [(137.3, 78.4, 78.4), (85.923,  -64.54, -93.114)]
    ])
    def test_solve(self, thetas: Tuple[float, float, float], expected: Tuple[float, float, float]):
        """Test that solver copmutes forward position

        Args:
            thetas (Tuple[float, float, float]): the input test theta rotations
            expected (Tuple[float, float, float]): the expected position output
        """
        config = self.__test_config__()
        
        pos = ForwardKinematicGraphicalArachneSolver.solve(config, thetas)

        nptest.assert_almost_equal(expected, pos, decimal = 3)

    def __test_config__(self) -> LegConfig:
        """Mock frame data

        Returns:
            LegConfig: mock config
        """
        return LegConfig(66.0, 31.0, 77.0)
