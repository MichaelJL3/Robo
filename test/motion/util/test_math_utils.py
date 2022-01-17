
"""Math utilities tests"""

import unittest

from parameterized import parameterized

from src.motion.util.math_utils import loc_theta_degrees, loc_degrees, pythagorean_side

class TestMathUtils(unittest.TestCase):
    @parameterized.expand([
        [3, 4, 60, 3.60],
        [3, 3, 90, 4.24]
    ])
    def test_law_of_cosines(self, side_a: float, side_b: float, theta: float, expected: float):
        """Test frame transforms

        Args:
            side_a (float): side of the triangle
            side_b (float): side of the triangle
            theta (float): theta of side c
            expected (float): missing side
        """
        result = loc_degrees(side_a, side_b, theta)
        self.assertAlmostEqual(expected, result, places=1)

    @parameterized.expand([
        [3, 4, 5, 90],
        [3, 3, 3, 60]
    ])
    def test_law_of_cosines_angle(self, side_a: float, side_b: float, side_c: float, expected: float):
        """Test frame transforms

        Args:
            side_a (float): side of the triangle
            side_b (float): side of the triangle
            side_c (float): side of the triangle
            expected (float): theta of side c
        """
        result = loc_theta_degrees(side_a, side_b, side_c)
        self.assertAlmostEqual(expected, result, places=3)

    @parameterized.expand([
        [3, 5, 4],
        [10.5, 16.17, 12.29]
    ])
    def test_pythagorean_side(self, side_a: float, hypotenuse: float, expected: float):
        """Test frame transforms

        Args:
            a (float): side of the triangle
            c (float): hypotenuse of the triangle
            expected (float): missing side
        """
        result = pythagorean_side(side_a, hypotenuse)
        self.assertAlmostEqual(expected, result, places=1)
