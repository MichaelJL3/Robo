
"""Move controller tests"""

import unittest
from unittest.mock import Mock, create_autospec

import numpy as nd
import numpy.testing as nptest

from arachnid.move.move_controller import MoveController

from robotics.body.part import Part
from robotics.body.leg_3dof import Leg3DOF
from robotics.motion.gait.gait import Gait
from robotics.typings.types import PositionGenerator

class TestMoveController(unittest.TestCase):
    """Move controller tests"""

    @staticmethod
    def __gen__() -> PositionGenerator:
        """Mock generator for walking

        Yields:
            PositionGenerator: the movement position
        """
        yield (66, 108.0, 0)

    @staticmethod
    def __controller_helper__() -> MoveController:
        """Construct move controller with mocks

        Returns:
            MoveController: the move controller
        """
        gait = create_autospec(Gait)
        gait.walking_generator.return_value = TestMoveController.__gen__()
        gait.turning_generator.return_value = TestMoveController.__gen__()

        kinematics = Mock()
        kinematics.return_value = (90.0, 0.0, 0.0)

        parts = [ Part(Leg3DOF(66.0, 31.0, 77.0), (90, 90, 90), 0, 0) ]
        motions = [.5, .5]

        return MoveController(gait, kinematics, parts, motions)

    def test_walking(self):
        """Test walking sequence"""
        move_controller = TestMoveController.__controller_helper__()
        walking = move_controller.walking()

        expected = [[[ 90.,  45., 45.],[ 90.,  45., 45.]]]

        step = next(walking)
        self.assertEqual((1,2,3), step.shape)
        nptest.assert_almost_equal(expected, step, decimal = 3)

    def test_turning(self):
        """Test turning sequence"""
        move_controller = TestMoveController.__controller_helper__()
        turning = move_controller.turning()

        expected = [[[ 90.,  45., 45.],[ 90.,  45., 45.]]]

        step = next(turning)
        self.assertEqual((1,2,3), step.shape)
        nptest.assert_almost_equal(expected, step, decimal = 3)

    def test_rotation_iter(self):
        """Test iteration order of rotation step through"""
        mtx = nd.array([[[1, 0, 0]], [[0, 1, 1]], [[0, 0, 0]], [[0, 1, 0]]])

        expected = [
            (0, 1),(3, 0),(6,  0),(9, 0),
            (1, 0),(4, 1),(7, 0),(10, 1),
            (2, 0),(5, 1),(8, 0),(11, 0)
        ]

        mv_it = MoveController.rotation_iter(mtx)

        self.assertEqual(expected, list(mv_it))
