
"""Frame tests"""

import unittest

from src.motion.frame import Frame

class TestFrame(unittest.TestCase):
    """Frame tests"""

    def test_required_variables_exist(self):
        """Testing only to ensure the 4 minimum frame requirements for DH are defined"""
        frame = Frame(1, 1, 1, 1)
        self.assertEqual(1, frame.delta)
        self.assertEqual(1, frame.rho)
        self.assertEqual(1, frame.theta)
        self.assertEqual(1, frame.alpha)

    def test_frame_concat(self):
        """Testing that concat combines two frames statically"""
        frame_a = Frame(7, -10, 10, 40)
        frame_b = Frame(3, 30, 20, 0)
        result = Frame.combine(frame_a, frame_b)
        expected = Frame(10, 20, 30, 40)

        self.assertEqual(expected, result)

    def test_frame_concat_relative(self):
        """Testing that concat combines two frames from one reference frame"""
        frame_a = Frame(7, -10, 10, 40)
        frame_b = Frame(3, 30, 20, 0)
        result = frame_a + frame_b
        expected = Frame(10, 20, 30, 40)

        self.assertEqual(expected, result)

    def test_frame_concat_is_immutable(self):
        """Test that frame concat is immutable"""
        frame_a = Frame(7, -10, 10, 40)
        frame_b = Frame(3, 30, 20, 0)
        frame_c = Frame.combine(frame_a, frame_b)

        self.assertNotEqual(frame_c, frame_a)
        self.assertNotEqual(frame_c, frame_b)

    def test_frame_concat_relative_is_immutable(self):
        """Test that frame concat from one reference frame is immutable"""
        frame_a = Frame(7, -10, 10, 40)
        frame_b = Frame(3, 30, 20, 0)
        frame_c = frame_a + frame_b

        self.assertNotEqual(frame_c, frame_a)
        self.assertNotEqual(frame_c, frame_b)
