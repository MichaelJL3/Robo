
"""Smoothing tests"""

import unittest

from robotics.motion.smoothing import Smoothing

class TestSmoothing(unittest.TestCase):
    """Smoothing tests"""

    def test_default_motion(self):
        """Check that default smoothing is applied"""
        expected = [.02, .05, .10, .25, .50, .75, .90, .95, .98, 1]
        smoothing = Smoothing()

        self.assertEqual(expected, smoothing.motion)

    def test_override_motion(self):
        """Check that default smoothing is applied"""
        expected = [.05, .05]
        smoothing = Smoothing(expected)

        self.assertEqual(expected, smoothing.motion)

    def test_no_smoothing_needed(self):
        """Test no smoothing needed smoothing"""
        smoothing = Smoothing([.5, 1])
        curr = (90, 90, 90)
        new = (90, 90, 90)
        result = smoothing.smooth(curr, new)
        expected = [(90.0, 90.0, 90.0),(90.0, 90.0, 90.0)]

        self.assertEqual(expected, result)

    def test_smoothing_needed(self):
        """Test no smoothing needed smoothing"""
        smoothing = Smoothing([.3, .7, 1])
        curr = (90, 90, 90)
        new = (45, 45, 45)
        result = smoothing.smooth(curr, new)
        expected = [(76.5, 76.5, 76.5), (58.5, 58.5, 58.5), (45, 45, 45)]

        self.assertEqual(expected, result)

    def test_as_function_call(self):
        """Test smoothing called as function"""
        smoothing = Smoothing([.3, .7, 1])
        curr = (90, 90, 90)
        new = (45, 45, 45)
        result = smoothing(curr, new)
        expected = [(76.5, 76.5, 76.5), (58.5, 58.5, 58.5), (45, 45, 45)]

        self.assertEqual(expected, result)
