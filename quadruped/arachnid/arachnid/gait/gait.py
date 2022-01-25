
"""Gait generation for movements"""

from abc import abstractmethod

from robotics.typings.types import GaitProvider
from robotics.typings.types import PositionGenerator
from robotics.typings.types import Vector3
from robotics.decorators.decorators import closure

class Gait():
    """Gait class"""

    def forward(self, index: int = 0) -> GaitProvider:
        """Forward gait

        Args:
            index (int, optional): the starting position in the gait. Defaults to 0.

        Returns:
            GaitProvider: provider which always starts the gait at index
        """
        return closure(self.walking_generator)(index)

    def backward(self, index: int = 0) -> GaitProvider:
        """Backward gait

        Args:
            index (int, optional): the starting position in the gait. Defaults to 0.

        Returns:
            GaitProvider: provider which always starts the gait at index
        """
        return closure(self.walking_generator)(index, True)

    def turn_right(self, index: int = 0) -> GaitProvider:
        """Right turn gait

        Args:
            index (int, optional): the starting position in the gait. Defaults to 0.

        Returns:
            GaitProvider: provider which always starts the gait at index
        """
        return closure(self.turning_generator)(index)

    def turn_left(self, index: int = 0) -> GaitProvider:
        """Left turn gait

        Args:
            index (int, optional): the starting position in the gait. Defaults to 0.

        Returns:
            GaitProvider: provider which always starts the gait at index
        """
        return closure(self.turning_generator)(index, True)

    @abstractmethod
    def __gait_provider__(self, _: int, __: bool = False) -> Vector3:
        """Provide the gait at the index

        Args:
            _ (int): the passed in index.
            __ (bool, optional): the reverse flag. Defaults to False

        Raises:
            NotImplementedError: must be extended

        Returns:
            Vector3: the gait position
        """
        raise NotImplementedError()

    def turning_generator(self, start: int = 0, reverse: bool = False) -> PositionGenerator:
        """Rotating generator for turn based gait

        Args:
            start (int, optional): the initial step index. Defaults to 0.
            reverse (bool, optional): whether to reverse the direction. Defaults to false.

        Yields:
            PositionGenerator: the leg position
        """
        allowed_index = [0, 1, 4, 7]

        if start not in allowed_index:
            raise ValueError(f'Start index must be in {allowed_index}')

        i = start
        while True:
            yield self.__gait_provider__(i, reverse)
            i = (i + 3) % 10 if i != 0 else 1

    def walking_generator(self, start: int = 0, reverse: bool = False) -> PositionGenerator:
        """Rotating generator for walking gait

        Args:
            start (int, optional): the initial step index. Defaults to 0.
            reverse (bool, optional): whether to reverse the direction. Defaults to false.

        Yields:
            PositionGenerator: the leg position
        """
        if start > 7 or start < 0:
            raise ValueError("Start index must be between [0-8)")

        i = start
        while True:
            yield self.__gait_provider__(i, reverse)
            i = (i + 1) % 8
