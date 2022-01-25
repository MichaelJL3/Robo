
"""Locomotion tests"""

import unittest
from unittest.mock import MagicMock, Mock

import numpy as nd
import numpy.testing as nptest

from robotics.motion.locomotion import LocomotionController
from robotics.motion.locomotion import PartLocomotion
from robotics.motion.mapping import CommonMotions

class TestPartLocomotion(unittest.TestCase):
    """Locomotion part tests"""

    def test_init_part(self):
        """Test initial part"""
        part = Mock()
        motor = PartLocomotion(part, {}, None, None)

        self.assertEqual(part, motor.part)

    def test_start(self):
        """Test start"""
        part = Mock()
        kinematics = Mock()
        mapping = MagicMock()
        smooth = MagicMock()

        mapping.__getitem__().return_value = [(90, 90, 90)]
        smooth.return_value = [(90, 90, 90)]

        motor = PartLocomotion(part, mapping, kinematics, smooth)
        result = next(motor.start(CommonMotions.FORWARD))
        expected = [(90, 90, 90)]

        self.assertEqual(expected, result)

    def test_start_does_nothing_until_iterated(self):
        """Test """
        motor = PartLocomotion(None, {}, None, None)
        result = motor.start(CommonMotions.FORWARD)

        self.assertIsNotNone(result)

    def test_missing_motion_throws(self):
        """Test missing motion throws"""
        motor = PartLocomotion(None, {}, None, None)
        result = motor.start(CommonMotions.FORWARD)

        with self.assertRaises(KeyError):
            next(result)

class TestLocomotionController(unittest.TestCase):
    """Locomotion controller tests"""

    def test_init_locomotors(self):
        """Test initial motors"""
        motors = [Mock(), Mock()]
        controller = LocomotionController(motors)

        self.assertEqual(motors, controller.locomotors)

    def test_start(self):
        """Test start"""
        motor_a = MagicMock()
        motor_b = MagicMock()
        motor_a.start().__next__.return_value = [1, 2]
        motor_b.start().__next__.return_value = [3, 4]
        motors = [motor_a, motor_b]

        controller = LocomotionController(motors)
        result = next(controller.start(CommonMotions.FORWARD))
        expected = nd.array([[1, 2], [3, 4]])

        self.assertEqual(expected.shape, result.shape)
        nptest.assert_equal(expected, result)
