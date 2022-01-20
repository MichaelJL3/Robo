
"""Move controller"""

from typing import Generator, List, Tuple

import numpy as nd

from motion.leg_state import LegState
from gait.gait import Gait

import motion.kinematics.graphical_arachne as gkinematics

Matrix2D = List[List[float]]
Matrix3D = List[Matrix2D]
Position = Tuple[float, float, float]
PositionGenerator = Generator[Position, None, None]

class MoveController:
    """Move controller class"""

    _pre_defined_arc = [.02, .05, .10, .25, .50, .75, .90, .95, .98, 1]

    def __init__(self, gait: Gait, legs: List[LegState], motion: List[float] = None):
        self._gait = gait
        self._legs = legs
        self._motion = motion if motion else self._pre_defined_arc

    def walking(self) -> PositionGenerator:
        """Get the steps needed to complete the next step accross all legs

        Yields:
            PositionGenerator: the matrix of actions
        """
        while True:
            yield nd.array(list((map(lambda leg: \
                self.__motion_arc__(self._gait.walking_generator(leg.walking_id), leg), \
                self._legs))))

    def turning(self) -> PositionGenerator:
        """Get the steps needed to complete the next step accross all legs

        Yields:
            PositionGenerator: the matrix of actions
        """
        while True:
            yield nd.array(list((map(lambda leg: \
                self.__motion_arc__(self._gait.turning_generator(leg.turning_id), leg), \
                self._legs))))

    @staticmethod
    def rotation_iter(moves: Matrix3D) -> Tuple[int, float]:
        """Create an iterator over the 3d matrix of smoothed motions among all legs

        Args:
            moves (Matrix3D): the input matrix

        Yields:
            Tuple[int, float]: the tag of servo to the rotation
        """
        legs, motions, parts_per_leg = moves.shape

        for motion in range(motions):
            for part in range(parts_per_leg):
                for leg in range(legs):
                    yield (leg * parts_per_leg + part, moves[leg, motion, part])

    def __split_motion__(self, current_pos: Position, new_pos: Position) -> Matrix2D:
        """Smoothen the rotation by splitting it into smaller parts

        Args:
            current_pos (Position): the current position
            new_pos (Position): the destination position

        Returns:
            Matrix2D: the split moves between current and destination
        """
        moves = []

        c_x, c_y, c_z = current_pos
        n_x, n_y, n_z = new_pos

        for pct in self._motion:
            move_a = c_x + (n_x - c_x) * pct
            move_b = c_y + (n_y - c_y) * pct
            move_c = c_z + (n_z - c_z) * pct
            moves.append((move_a, move_b, move_c))

        return moves

    def __motion_arc__(self, gen: PositionGenerator, state: LegState) -> Matrix2D:
        """get the smoothed rotations for the given movement strategy

        Args:
            gen (PositionGenerator): the destination generator
            state (LegState): the legs state

        Returns:
            Matrix2D: the matrix of smoothed motions to reach the destination
        """
        thetas = gkinematics.solve_inverse_kinematic(state.config, next(gen))
        motion = self.__split_motion__(state.position, thetas)
        state.position = thetas
        return motion
