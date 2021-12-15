
from __future__ import annotations
from .joint import Joint

class ArachneLegBuilder(object):
    """Arachne leg builder"""

    def hip(self, hip: Joint) -> ArachneLegBuilder:
        """Add a hip joint for the leg

        Args:
            hip (Joint): The hip joint

        Returns:
            ArachneLegBuilder: The leg builder
        """
        self.hip = hip
        return self

    def knee(self, knee: Joint) -> ArachneLegBuilder:
        """Add a knee joint for the leg

        Args:
            knee (Joint): The knee joint

        Returns:
            ArachneLegBuilder: The leg builder
        """
        self.knee = knee
        return self

    def foot(self, foot: Joint) -> ArachneLegBuilder:
        """Add a foot joint for the leg

        Args:
            foot (Joint): The foot joint

        Returns:
            ArachneLegBuilder: The leg builder
        """
        self.foot = foot
        return self

    def build(self) -> ArachneLeg:
        """Build the new arachne leg

        Returns:
            ArachneLeg: The new leg
        """
        return ArachneLeg(self.hip, self.knee, self.foot)

class ArachneLeg(object):
    """Arachne leg"""

    def __init__(self, hip: Joint, knee: Joint, foot: Joint):
        """Constructor

        Args:
            hip  (Joint): The hip joint
            knee (Joint): The knee joint
            foot (Joint): The foot joint
        """
        self.hip = hip
        self.knee = knee
        self.foot = foot

    def set_hip_angle(self, angle: float) -> ArachneLeg:
        """Set the angle for the hip joint

        Args:
            angle (float): The angle to set

        Returns:
            ArachneLeg: The leg
        """
        self.hip.angle = angle
        return self

    def set_knee_angle(self, angle: float) -> ArachneLeg:
        """Set the angle for the knee joint

        Args:
            angle (float): The angle to set

        Returns:
            ArachneLeg: The leg
        """
        self.knee.angle = angle
        return self

    def set_foot_angle(self, angle: float) -> ArachneLeg:
        """Set the angle for the foot joint

        Args:
            angle (float): The angle to set

        Returns:
            ArachneLeg: The leg
        """
        self.foot.angle = angle
        return self

    def offset_hip_angle(self, angle: float) -> ArachneLeg:
        """Offset the angle for the hip joint

        Args:
            angle (float): The angle to offset

        Returns:
            ArachneLeg: The leg
        """
        self.hip.angle += angle
        return self

    def offset_knee_angle(self, angle: float) -> ArachneLeg:
        """Offset the angle for the knee joint

        Args:
            angle (float): The angle to offset

        Returns:
            ArachneLeg: The leg
        """
        self.knee.angle += angle
        return self

    def offset_foot_angle(self, angle: float) -> ArachneLeg:
        """Offset the angle for the foot joint

        Args:
            angle (float): The angle to offset

        Returns:
            ArachneLeg: The leg
        """
        self.foot.angle += angle
        return self

    def set_angles(self, hip_angle: float, knee_angle: float, foot_angle: float) -> ArachneLeg:
        """Sets the angles for all the leg joints

        Args:
            hip_angle  (float): The hip angle to set
            knee_angle (float): The knee angle to set
            foot_angle (float): The foot angle to set

        Returns:
            ArachneLeg: The leg
        """
        return self.set_hip_angle(hip_angle) \
            .set_knee_angle(knee_angle) \
            .set_foot_angle(foot_angle)

    def offset_angles(self, hip_angle: float, knee_angle: float, foot_angle: float) -> ArachneLeg:
        """Adds increments to the angles for all the leg joints

        Args:
            hip_angle  (float): The hip angle to offset
            knee_angle (float): The knee angle to offset
            foot_angle (float): The foot angle to offset

        Returns:
            ArachneLeg: The leg
        """
        return self.offset_hip_angle(hip_angle) \
            .offset_knee_angle(knee_angle) \
            .offset_foot_angle(foot_angle)

    def get_angles(self):
        """Get the current set of joint angles

        Returns:
            Triple: The triple of joint angles
        """
        return (self.hip.angle, self.knee.angle, self.foot.angle)
