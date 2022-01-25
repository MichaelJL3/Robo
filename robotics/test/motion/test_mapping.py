
"""Mapping tests"""

import unittest
from unittest.mock import MagicMock, Mock, create_autospec

from robotics.body.part import Part
from robotics.motion.mapping import CommonMotionsMapping
from robotics.motion.mapping import MotionMapping
from robotics.motion.mapping import CommonMotions
from robotics.typings.types import GeneratorMap

class TestMotionMapping(unittest.TestCase):
    """Mapping tests"""

    def test_register(self):
        """test registration method"""
        part = create_autospec(Part)
        part.name = 'test'
        part_mapping = Mock()

        mapping = MotionMapping()
        mapping.register(part, part_mapping)
        result = mapping[part]

        self.assertEqual(part_mapping, result)

    def test_register_as_operator(self):
        """test registration method"""
        part = create_autospec(Part)
        part.name = 'test'
        part_mapping = Mock()

        mapping = MotionMapping()
        mapping[part] = part_mapping
        result = mapping[part]

        self.assertEqual(part_mapping, result)

    def test_get_part_mapping(self):
        """test getting map"""
        part = create_autospec(Part)
        part.name = 'test'
        part_mapping = Mock()

        mapping = MotionMapping({ 'test': part_mapping })
        result = mapping.get_part_mapping(part)

        self.assertEqual(part_mapping, result)

    def test_get_motion(self):
        """test getting motion"""
        expected = 5
        part = create_autospec(Part)
        motion_map = MagicMock()
        motion_map.get().get.return_value = expected

        mapping = MotionMapping(motion_map)
        result = mapping.get_part_motion(part, CommonMotions.FORWARD)

        self.assertEqual(expected, result)

    def test_get_motion_by_name(self):
        """test getting motion"""
        expected = {}
        motion_map = MagicMock()
        motion_map.get.return_value = expected

        mapping = MotionMapping(motion_map)
        result = mapping.get_part_mapping_by_name('test')

        self.assertEqual(expected, result)

class TestCommonMotionMapping(unittest.TestCase):
    """Common mapping tests"""

    @staticmethod
    def _motion_helper(expected: int) -> GeneratorMap:
        """Get a mocked motion helper

        Args:
            expected (int): the expected output

        Returns:
            GeneratorMap: helper mapping
        """
        part_map = MagicMock()
        part_map.get().__getitem__().return_value = expected

        return part_map

    def test_forward(self):
        """test forward"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.forward(Mock())

        self.assertEqual(expected, motion())

    def test_backward(self):
        """test backward"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.backward(Mock())

        self.assertEqual(expected, motion())

    def test_left(self):
        """test left"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.left(Mock())

        self.assertEqual(expected, motion())

    def test_right(self):
        """test right"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.right(Mock())

        self.assertEqual(expected, motion())

    def test_turn_left(self):
        """test turn left"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.turn_left(Mock())

        self.assertEqual(expected, motion())

    def test_turn_right(self):
        """test turn right"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.turn_right(Mock())

        self.assertEqual(expected, motion())

    def test_diag_left_forward(self):
        """test diagonal left forward"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.diag_left_forward(Mock())

        self.assertEqual(expected, motion())

    def test_diag_left_backward(self):
        """test diagonal left backward"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.diag_left_backward(Mock())

        self.assertEqual(expected, motion())

    def test_diag_right_forward(self):
        """test diagonal right backward"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.diag_right_forward(Mock())

        self.assertEqual(expected, motion())

    def test_diag_right_backward(self):
        """test diagonal right backward"""
        expected = 5
        motions = self._motion_helper(expected)
        mapping = CommonMotionsMapping(motions)
        motion = mapping.diag_right_backward(Mock())

        self.assertEqual(expected, motion())
