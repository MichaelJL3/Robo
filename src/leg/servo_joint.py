
from .joint import Joint

class ServoJoint(Joint):
    """A joint comprised of a servo"""

    def __init__(self, servo, min_angle: float = 0, max_angle: float = 180):
        """constructor

        Args:
            pin (float): The servo gpio pin
        """
        self.servo = servo
        self.min_angle = min_angle
        self.max_angle = max_angle

    @property
    def angle(self):
        """Get the angle of the servo

        Returns:
            int: The servo angle
        """
        return self.servo.angle

    @angle.setter
    def angle(self, angle: float):
        """Sets the angle of the servo

        Args:
            angle (float): The new angle value
        """
        self.servo.angle = min(max(angle, self.min_angle), self.max_angle)
