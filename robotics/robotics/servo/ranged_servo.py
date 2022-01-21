
"""Servo wrapper"""

from typing import Generic
from robotics.typings.types import Servo

class RangedServo:
    """Servo wrapper class bounding the movements between min/max angles"""

    def __init__(self, servo: Generic[Servo], min_angle: float = 0, max_angle: float = 180):
        """constructor

        Args:
            servo (Generic[Servo]): the wrapped servo
            min_angle (float, optional): [description]. Defaults to 0.
            max_angle (float, optional): [description]. Defaults to 180.
        """
        self._servo = servo
        self._min_angle = min_angle
        self._max_angle = max_angle

    @property
    def max_angle(self):
        """[summary]

        Returns:
            float: The maximum servo angle
        """
        return self._max_angle

    @max_angle.setter
    def max_angle(self, angle: float):
        """Sets the max angle of the servo

        Args:
            angle (float): The new max angle value
        """
        self._max_angle = angle

    @property
    def min_angle(self):
        """[summary]

        Returns:
            float: The minimum servo angle
        """
        return self._min_angle

    @min_angle.setter
    def min_angle(self, angle: float):
        """Sets the min angle of the servo

        Args:
            angle (float): The new min angle value
        """
        self._min_angle = angle

    @property
    def angle(self):
        """Get the angle of the servo

        Returns:
            float: The servo angle
        """
        return self._servo.angle

    @angle.setter
    def angle(self, angle: float):
        """Sets the angle of the servo

        Args:
            angle (float): The new angle value
        """
        self._servo.angle = min(max(angle, self._min_angle), self._max_angle)
