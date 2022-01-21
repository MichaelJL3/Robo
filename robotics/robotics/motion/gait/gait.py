
"""Gait generation for movements"""

from abc import abstractmethod

from robotics.typings.types import Position, PositionGenerator

class Gait:
    """Gait class"""

    @abstractmethod
    def __gait_provider__(self, _: int) -> Position:
        """[summary]

        Args:
            _ (int): will be the past in index

        Raises:
            NotImplementedError: must be extended

        Returns:
            Position: the gait position
        """
        raise NotImplementedError()

    @abstractmethod
    def turning_generator(self, start: int = 0) -> PositionGenerator:
        """Rotating generator for turn based gait

        Args:
            start (int, optional): the initial step index. Defaults to 0.

        Yields:
            PositionGenerator: the leg position
        """
        raise NotImplementedError()

    @abstractmethod
    def walking_generator(self, start: int = 0) -> PositionGenerator:
        """Rotating generator for walking gait

        Args:
            start (int, optional): the initial step index. Defaults to 0.

        Yields:
            PositionGenerator: the leg position
        """
        raise NotImplementedError()
