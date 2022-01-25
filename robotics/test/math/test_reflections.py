
"""Reflection utilities tests"""

from typing import List
import unittest

from parameterized import parameterized

from robotics.typings.types import Vector3
from robotics.math.reflections import (
    axis_3d, x_axis_3d, y_axis_3d, z_axis_3d,
    quadrant_2, quadrant_2_x, quadrant_2_y, quadrant_2_z
)

class TestReflections(unittest.TestCase):
    """Reflection utilities tests"""

    @parameterized.expand([
        [(30,  20, 10), (30,  20, -10)],
        [(150, 10, 50), (150, 10, -50)]
    ])
    def test_reflect_axis_3d_x(self, vec: Vector3, expected: Vector3):
        """test single axis around x reflection

        Args:
            vec (Vector3): the position
            expected (Vector3): the expected reflection
        """
        self.assertEqual(expected, x_axis_3d(vec))

    @parameterized.expand([
        [(30,  20, 10), (30,  -20, 10)],
        [(150, 10, 50), (150, -10, 50)]
    ])
    def test_reflect_axis_3d_y(self, vec: Vector3, expected: Vector3):
        """test single axis around y reflection

        Args:
            vec (Vector3): the position
            expected (Vector3): the expected reflection
        """
        self.assertEqual(expected, y_axis_3d(vec))

    @parameterized.expand([
        [(30,  20, 10), (-30,  20, 10)],
        [(150, 10, 50), (-150, 10, 50)]
    ])
    def test_reflect_axis_3d_z(self, vec: Vector3, expected: Vector3):
        """test single axis around z reflection

        Args:
            vec (Vector3): the position
            expected (Vector3): the expected reflection
        """
        self.assertEqual(expected, z_axis_3d(vec))

    @parameterized.expand([
        [(30,  20, 10), (-30,  -20, -10), [True,  True,  True]],
        [(150, 10, 50), (-150,  10, -50), [True,  False, True]],
        [(150, 10, 50), ( 150,  10, -50), [True,  False, False]],
        [(150, 10, 50), ( 150, -10,  50), [False, True,  False]]
    ])
    def test_reflect_axis_3d(self, vec: Vector3, expected: Vector3, flags: List[bool]):
        """test variable reflection

        Args:
            vec (Vector3): the position
            expected (Vector3): the reflected position
            flags (List[bool]): reflection flags
        """
        self.assertEqual(expected, axis_3d(vec, flags[0], flags[1], flags[2]))

    @parameterized.expand([
        [(30,  20, 10), (150, 20, 10)],
        [(150, 10, 50), (30,  10, 50)]
    ])
    def test_quadrant_reflection_x(self, vec: Vector3, expected: Vector3):
        """test quadrant 2 reflection around x

        Args:
            vec (Vector3): the rotations
            expected (Vector3): the expected reflection
        """
        self.assertEqual(expected, quadrant_2_x(vec))

    @parameterized.expand([
        [(30,  20, 10), (30,  160, 10)],
        [(150, 10, 50), (150, 170, 50)]
    ])
    def test_quadrant_reflection_y(self, vec: Vector3, expected: Vector3):
        """test quadrant 2 reflection around y

        Args:
            vec (Vector3): the rotations
            expected (Vector3): the expected reflection
        """
        self.assertEqual(expected, quadrant_2_y(vec))

    @parameterized.expand([
        [(30,  20, 10), (30,  20, 170)],
        [(150, 10, 50), (150, 10, 130)]
    ])
    def test_quadrant_reflection_z(self, vec: Vector3, expected: Vector3):
        """test quadrant 2 reflection around z

        Args:
            vec (Vector3): the rotations
            expected (Vector3): the expected reflection
        """
        self.assertEqual(expected, quadrant_2_z(vec))

    @parameterized.expand([
        [(30,  20, 10), (150, 160, 170), [True,  True,  True]],
        [(150, 10, 50), (30,  10,  130), [True,  False, True]],
        [(150, 10, 50), (30,  10,  50 ), [True,  False, False]],
        [(150, 10, 50), (150, 170, 50 ), [False, True,  False]]
    ])
    def test_quadrant_reflection(self, vec: Vector3, expected: Vector3, flags: List[bool]):
        """test variable rotations quadrant reflection

        Args:
            vec (Vector3): the position
            expected (Vector3): the reflected rotations
            flags (List[bool]): reflection flags
        """
        self.assertEqual(expected, quadrant_2(vec, flags[0], flags[1], flags[2]))
