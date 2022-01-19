
"""Gait tests"""

import unittest
from parameterized import parameterized

from src.gait.gait import Gait
from src.gait.gait_positional import GaitPositional
from src.gait.gait_rotational import GaitRotational

class TestGait(unittest.TestCase):
    """Gait tests"""

    gait_r = GaitRotational()
    gait_p = GaitPositional()

    @parameterized.expand([
        [gait_p],
        [gait_r]
    ])
    def test_walking_cycle(self, gait: Gait):
        """Test walking sequence cyclic period

        Args:
            gait (Gait): the gait
        """
        gen = gait.walking_generator()
        cycle_length = 8

        expected = [next(gen) for _ in range(cycle_length)]
        result = [next(gen) for _ in range(cycle_length)]

        self.assertEqual(expected, result)

    @parameterized.expand([
        [gait_p],
        [gait_r]
    ])
    def test_turning_cycle(self, gait: Gait):
        """Test turning sequence cyclic period

        Args:
            gait (Gait): the gait
        """
        gen = gait.turning_generator()
        cycle_length = 4

        expected = [next(gen) for _ in range(cycle_length)]
        result = [next(gen) for _ in range(cycle_length)]

        self.assertEqual(expected, result)

    @parameterized.expand([
        [gait_p, -1],
        [gait_p, -8],
        [gait_r, -1],
        [gait_r, -8],
    ])
    def test_walking_sequence_out_of_bounds_throws(self, gait: Gait, index: int):
        """Test walking sequence boundaries

        Args:
            index (int): the out of bound index
        """
        with self.assertRaises(ValueError):
            next(GaitRotational().walking_generator(index))

    @parameterized.expand([
        [gait_p, -1],
        [gait_p, 2],
        [gait_p, 3],
        [gait_p, 5],
        [gait_p, 6],
        [gait_p, 8],
        [gait_r, -1],
        [gait_r, 2],
        [gait_r, 3],
        [gait_r, 5],
        [gait_r, 6],
        [gait_r, 8]
    ])
    def test_turning_sequence_out_of_bounds_throws(self, gait: Gait, index: int):
        """Test turning sequence boundaries

        Args:
            index (int): the out of bound index
        """
        with self.assertRaises(ValueError):
            next(GaitRotational().turning_generator(index))
