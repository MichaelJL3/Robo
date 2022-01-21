
"""Gait tests"""

import unittest
from parameterized import parameterized

from arachnid.gait.gait import Gait

class TestGait(unittest.TestCase):
    """Gait tests"""

    def test_gait_position_throws_unimplemented(self):
        """Test that gait base class cannot be used directly"""
        with self.assertRaises(NotImplementedError):
            Gait().__gait_provider__(0)

    def test_walking_cycle(self):
        """Test walking sequence cyclic period"""
        gait = Gait()
        gait.__gait_provider__ = lambda x: x
        gen = gait.walking_generator()
        cycle_length = 8

        expected = [next(gen) for _ in range(cycle_length)]
        result = [next(gen) for _ in range(cycle_length)]

        self.assertEqual(expected, result)

    def test_turning_cycle(self):
        """Test turning sequence cyclic period"""
        gait = Gait()
        gait.__gait_provider__ = lambda x: x
        gen = gait.turning_generator()
        cycle_length = 4

        expected = [next(gen) for _ in range(cycle_length)]
        result = [next(gen) for _ in range(cycle_length)]

        self.assertEqual(expected, result)

    @parameterized.expand([[-1],[-8]])
    def test_walking_sequence_out_of_bounds_throws(self, index: int):
        """Test walking sequence boundaries

        Args:
            index (int): the out of bound index
        """
        with self.assertRaises(ValueError):
            next(Gait().walking_generator(index))

    @parameterized.expand([[-1],[2],[3],[5],[6],[8],])
    def test_turning_sequence_out_of_bounds_throws(self, index: int):
        """Test turning sequence boundaries

        Args:
            index (int): the out of bound index
        """
        with self.assertRaises(ValueError):
            next(Gait().turning_generator(index))
