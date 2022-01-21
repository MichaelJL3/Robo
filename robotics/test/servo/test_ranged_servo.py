
"""ranged servo tests"""

import unittest
from unittest.mock import MagicMock
from parameterized import parameterized

from robotics.servo.ranged_servo import RangedServo

class TestRangedServo(unittest.TestCase):
    """Ranged servo tests"""

    def test_initial_angle_ctor(self):
        """Test that min angle can be set via property"""
        min_angle = 10
        max_angle = 100

        servo = RangedServo(None, min_angle, max_angle)

        self.assertEqual(min_angle, servo.min_angle)
        self.assertEqual(max_angle, servo.max_angle)

    def test_min_angle_property(self):
        """Test that min angle can be set via property"""
        expected = 10

        servo = RangedServo(None, 0, 0)
        servo.min_angle = expected

        self.assertEqual(expected, servo.min_angle)

    def test_max_angle_property(self):
        """Test that min angle can be set via property"""
        expected = 100

        servo = RangedServo(None, 0, 0)
        servo.max_angle = expected

        self.assertEqual(expected, servo.max_angle)

    def test_angle_property(self):
        """Test that angle can be set via property"""
        expected = 100

        inner_servo = MagicMock()

        servo = RangedServo(inner_servo, 0, 180)
        servo.angle = expected

        self.assertEqual(expected, servo.angle)

    @parameterized.expand([
        [180,  210, 0, 180],
        [0,   -100, 0, 180],
        [50,   50,  0, 180],
        [90,   90,  0, 180],
        [180,  180, 0, 180]
    ])
    def test_angle_boundaries(self, \
        expected: float, angle: float, min_angle: float, max_angle: float):
        """Test that angle stays within boundaries"""

        inner_servo = MagicMock()

        servo = RangedServo(inner_servo, min_angle, max_angle)
        servo.angle = angle

        self.assertEqual(expected, servo.angle)
