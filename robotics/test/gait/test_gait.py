
"""Gait tests"""

import unittest

from robotics.motion.gait.gait import Gait

class TestGait(unittest.TestCase):
    """Gait tests"""

    def test_gait_position_throws_unimplemented(self):
        """Test that gait base class cannot be used directly"""
        with self.assertRaises(NotImplementedError):
            Gait().__gait_provider__(0)

    def test_walking_cycle_throws_unimplemented(self):
        """Test walking sequence cyclic period"""
        with self.assertRaises(NotImplementedError):
            Gait().walking_generator(0)

    def test_turning_cycle_throws_unimplemented(self):
        """Test turning sequence cyclic period"""
        with self.assertRaises(NotImplementedError):
            Gait().walking_generator(0)
