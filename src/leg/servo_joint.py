
from gpiozero import Servo
from joint import Joint

import math

class ServoJoint(Joint):
    """A joint comprised of a servo"""

    __MAX_ANGLE: float = 1
    __MIN_ANGLE: float = -1

    def __init__(self, pin: int):
        """constructor

        Args:
            pin (int): The servo gpio pin
        """
        self.servo = Servo(pin)

    @property
    def angle(self):
        """Get the angle of the servo

        Returns:
            int: The servo angle
        """
        return self.servo.value

    @angle.setter
    def angle(self, angle: float):
        """Sets the angle of the servo

        Args:
            angle (float): The new angle value
        """
        self.servo.value = math.min(math.max(angle, self.__MIN_ANGLE), self.__MAX_ANGLE)
