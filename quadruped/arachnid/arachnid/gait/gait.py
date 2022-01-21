
"""Gait generation for movements"""

from abc import abstractmethod
from typing import Generator, Tuple

from robotics.motion.gait.gait import Gait as GaitBase

Position = Tuple[float, float, float]
PositionGenerator = Generator[Position, None, None]

class Gait(GaitBase):
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

    def turning_generator(self, start: int = 0) -> PositionGenerator:
        """Rotating generator for turn based gait

        Args:
            start (int, optional): the initial step index. Defaults to 0.

        Yields:
            PositionGenerator: the leg position
        """
        allowed_index = [0, 1, 4, 7]

        if start not in allowed_index:
            raise ValueError(f'Start index must be in {allowed_index}')

        i = start
        while True:
            yield self.__gait_provider__(i)
            i = (i + 3) % 10 if i != 0 else 1

    def walking_generator(self, start: int = 0) -> PositionGenerator:
        """Rotating generator for walking gait

        Args:
            start (int, optional): the initial step index. Defaults to 0.

        Yields:
            PositionGenerator: the leg position
        """
        if start > 7 or start < 0:
            raise ValueError("Start index must be between [0-8)")

        i = start
        while True:
            yield self.__gait_provider__(i)
            i = (i + 1) % 8
