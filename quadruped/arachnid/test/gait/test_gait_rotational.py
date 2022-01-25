
"""Gait tests"""

import unittest
from parameterized import parameterized

from arachnid.gait.gait_rotational import GaitRotational
from robotics.typings.types import Vector3

class TestGaitRotational(unittest.TestCase):
    """Gait tests"""

    @parameterized.expand([
        [(90,  13, 13), 0],
        [(140, 90, 90), 1],
        [(130, 90, 90), 2],
        [(110, 90, 90), 3],
        [(90,  90, 90), 4],
        [(70,  90, 90), 5],
        [(50,  90, 90), 6],
        [(30,  90, 90), 7]
    ])
    def test_gait_provider(self, expected: Vector3, index: int):
        """Test gait provider

        Args:
            expected (Vector3): the expected position sequence
            index (int): the move index
        """
        res = GaitRotational().__gait_provider__(index)

        self.assertEqual(expected, res)

    @parameterized.expand([
        [(90,  13, 13), 0],
        [(40, 90, 90), 1],
        [(50, 90, 90), 2],
        [(70, 90, 90), 3],
        [(90,  90, 90), 4],
        [(110,  90, 90), 5],
        [(130,  90, 90), 6],
        [(150,  90, 90), 7]
    ])
    def test_gait_provider_reversed(self, expected: Vector3, index: int):
        """Test gait provider reversed

        Args:
            expected (Vector3): the expected position sequence
            index (int): the move index
        """
        res = GaitRotational().__gait_provider__(index, True)

        self.assertEqual(expected, res)

    @parameterized.expand([
        [(90,  13, 13), 0],
        [(140, 90, 90), 1],
        [(130, 90, 90), 2],
        [(110, 90, 90), 3],
        [(90,  90, 90), 4],
        [(70,  90, 90), 5],
        [(50,  90, 90), 6],
        [(30,  90, 90), 7]
    ])
    def test_walking_sequence(self, expected: Vector3, index: int):
        """Test walking sequence

        Args:
            expected (Vector3): the expected position sequence
            index (int): the move index
        """
        gen = GaitRotational().walking_generator(index)
        res = next(gen)

        self.assertEqual(expected, res)

    @parameterized.expand([
        [(90,  13, 13), 0],
        [(140, 90, 90), 1],
        [(90,  90, 90), 4],
        [(30,  90, 90), 7]
    ])
    def test_turning_sequence(self, expected: Vector3, index: int):
        """Test turn sequence

        Args:
            expected (Vector3): the expected position sequence
            index (int): the move index
        """
        gen = GaitRotational().turning_generator(index)
        res = next(gen)

        self.assertEqual(expected, res)
