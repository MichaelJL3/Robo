
from .joint import Joint

class ReversedJoint(Joint):
    def __init__(self, joint: Joint, max_angle: float = 180):
        """Constructor

        Args:
            joint (Joint): The wrapped joint
            max_angle (float, optional): The max angle. Defaults to 180.
        """
        self.joint = joint
        self.max_angle = max_angle

    @property
    def angle(self):
        """Get the angle of the joint

        Returns:
            int: The joint angle
        """
        return self.max_angle - self.joint.angle

    @angle.setter
    def angle(self, angle: float):
        """Sets the angle of the joint

        Args:
            angle (float): The new angle value
        """
        self.joint.angle = self.max_angle - angle
