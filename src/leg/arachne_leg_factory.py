
from .joint import Joint
from .arachne_leg import ArachneLegBuilder
from .servo_joint import ServoJoint
from .reversed_joint import ReversedJoint

class ArachneLegFactory(object):
    """Leg factory"""

    def __init__(self, servos):
        """Constructor

        Args:
            servos (Array): The array of servos
        """
        self.servos = servos

    def build(self, hip_pin:int, knee_pin: int, foot_pin: int, reverse_hip: bool = False, reverse_knee: bool = False, reverse_foot: bool = False):
        """Build a new leg from the kwargs dictionary
            the location of each servo
            whether the servos needs reversing

        Args:
            hip_pin  (int): The pin of the hip servo
            knee_pin (int): The pin of the knee servo
            foot_pin (int): The pin of the foot servo
            reverse_hip  (bool, optional): Reverse the hip servo. Defaults to False.
            reverse_knee (bool, optional): Reverse the knee servo. Defaults to False.
            reverse_foot (bool, optional): Reverse the foot servo. Defaults to False.

        Returns:
            ArachneLeg: The new leg 
        """
        hip  = self.__reverse__(ServoJoint(self.servos[hip_pin]),  reverse_hip)
        knee = self.__reverse__(ServoJoint(self.servos[knee_pin]), reverse_knee)
        foot = self.__reverse__(ServoJoint(self.servos[foot_pin]), reverse_foot)

        return ArachneLegBuilder() \
            .hip(hip) \
            .knee(knee) \
            .foot(foot) \
            .build()

    def __reverse__(self, joint: Joint, should_reverse: bool = False):
        """Check that joint should be reversed and then reverse if applicable

        Args:
            joint (Joint): The joint
            should_reverse (bool, optional): Whether the joint should be reversed. Defaults to False.

        Returns:
            Joint: The possibly reversed joint
        """
        return ReversedJoint(joint) if should_reverse else joint
