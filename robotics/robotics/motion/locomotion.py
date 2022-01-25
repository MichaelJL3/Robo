
"""Locomotion classes"""

from typing import List

import numpy as nd

from robotics.body.part import Part
from robotics.motion.smoothing import Smoothing
from robotics.typings.types import PositionGenerator
from robotics.typings.types import Kinematics
from robotics.typings.types import GeneratorMap

class PartLocomotion:
    """Part locomotion class"""

    def __init__(self, part: Part, moves: GeneratorMap, kinematics: Kinematics, \
        smoothing: Smoothing = None):
        """constructor

        Args:
            part (Part): the part under motion
            kinematics (Kinematics): the kinematic strategy
            move_map (GeneratorMap): the map of movement generator functions
            smoothing (Smoothing, optional): the smoothing function to split the rotation
        """
        self._part = part
        self._moves = moves
        self._kinematics = kinematics
        self._smoothing = smoothing if smoothing else Smoothing()

    @property
    def part(self) -> Part:
        """Get the underlying part

        Returns:
            Part: the part
        """
        return self._part

    def start(self, motion: str) -> PositionGenerator:
        """Start the motion

        Args:
            motion (str): the motion

        Returns:
            PositionGenerator: the generator for positions
        """
        for destination in self._moves[motion]():
            thetas = self._kinematics(self._part.config, destination)
            motion = self._smoothing(self._part.position, thetas)
            self._part.position = thetas
            yield motion

class LocomotionController:
    """Locomotion controller class"""

    def __init__(self, locomotors: List[PartLocomotion]):
        """constructor

        Args:
            locomotors (List[PartLocomotion]): the locomotors
        """
        self._locomotors = locomotors

    @property
    def locomotors(self) -> List[PartLocomotion]:
        """Get the locomotors

        Returns:
            List[PartLocomotion]: the locomotors
        """
        return self._locomotors

    def start(self, motion: str) -> PositionGenerator:
        """Start the motion

        Args:
            motion (str): the motion

        Returns:
            PositionGenerator: the combined motor position generator
        """
        motors = [locomotor.start(motion) for locomotor in self._locomotors]
        while True:
            computed_motions = [next(motor, None) for motor in motors]
            yield nd.array(computed_motions)
