
"""Gait tests"""

import unittest
from parameterized import parameterized

from arachnid.gait.gait_positional import GaitPositional
from robotics.typings.types import Position

class TestGaitPositional(unittest.TestCase):
    """Gait tests"""

    @parameterized.expand([
        [(106.73,  99.41,   0.00), 0],
        [( 62.35, -77.00,  74.31), 1],
        [( 74.31, -77.00, -62.35), 2],
        [( 91.15, -77.00, -33.18), 3],
        [( 97.00, -77.00,   0.00), 4],
        [( 91.15, -77.00,  33.18), 5],
        [( 74.31, -77.00,  62.35), 6],
        [( 48.50, -77.00,  84.00), 7]
    ])
    def test_walking_sequence(self, expected: Position, index: int):
        """Test walking sequence

        Args:
            expected (Position): the expected position sequence
            index (int): the move index
        """
        gen = GaitPositional().walking_generator(index)
        res = next(gen)

        self.assertEqual(expected, res)

    @parameterized.expand([
        [(106.73,  99.41,   0.00), 0],
        [( 62.35, -77.00,  74.31), 1],
        [( 97.00, -77.00,   0.00), 4],
        [( 48.50, -77.00,  84.00), 7]
    ])
    def test_turning_sequence(self, expected: Position, index: int):
        """Test turn sequence

        Args:
            expected (Position): the expected position sequence
            index (int): the move index
        """
        gen = GaitPositional().turning_generator(index)
        res = next(gen)

        self.assertEqual(expected, res)
