
"""Gait generation for movements"""

from abc import abstractmethod
from typing import Tuple

class Gait:
    """Gait class"""

    @abstractmethod
    def __gait_provider__(self, _: int) -> Tuple[float, float, float]:
        """[summary]

        Args:
            _ (int): will be the past in index

        Raises:
            NotImplementedError: must be extended

        Returns:
            Tuple[float, float, float]: the gait position
        """
        raise NotImplementedError()

    def turning_generator(self, start: int = 0) -> Tuple[float, float, float]:
        """Rotating generator for turn based gait

        Args:
            start (int, optional): the initial step index. Defaults to 0.

        Yields:
            Tuple[float, float, float]: the leg position
        """
        allowed_index = [0, 1, 4, 7]

        if start not in allowed_index:
            print("out of bounds")
            raise ValueError(f'Start index must be in {allowed_index}')

        i = start
        while True:
            yield self.__gait_provider__(i)
            i = (i + 3) % 10 if i != 0 else 1

    def walking_generator(self, start: int = 0) -> Tuple[float, float, float]:
        """Rotating generator for walking gait

        Args:
            start (int, optional): the initial step index. Defaults to 0.

        Yields:
            Tuple[float, float, float]: the leg position
        """
        if start > 7 or start < 0:
            print("out of bounds")
            raise ValueError("Start index must be between [0-8)")

        i = start
        while True:
            yield self.__gait_provider__(i)
            i = (i + 1) % 8
