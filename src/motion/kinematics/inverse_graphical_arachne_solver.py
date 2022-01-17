
import math

from typing import Tuple
from ..leg_config import LegConfig
from ..util.math_utils import loc_theta_degrees

class InverseKinematicGraphicalArachneSolver(object):
    """Inverse kinematics graphical solver for quadruped"""

    @staticmethod
    def solve(config: LegConfig, dst: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """Calculate the inverse kinematics for a graphically mapped arache leg (3DOF)

        Args:
            config (LegConfig): the leg configuration
            dst (Tuple[float, float, float]): the desired location relative to the leg base

        Returns:
            Tuple[float, float, float]: the required theta rotations to reach desired location
        """

        coaxia_length = config.coaxia_length
        femur_length  = config.femur_length
        tibia_length  = config.tibia_length

        x, y, z = dst

        diagonal_length = math.hypot(x, z)

        inner_base = diagonal_length - coaxia_length
        inner_hypotenuse = math.hypot(inner_base, y)

        alpha_1 = math.degrees(math.acos(y / inner_hypotenuse))
        alpha_2 = loc_theta_degrees(femur_length, inner_hypotenuse, tibia_length)

        theta_1 = math.degrees(math.atan2(x, z))
        theta_2 = alpha_1 - alpha_2
        theta_3 = loc_theta_degrees(femur_length, tibia_length, inner_hypotenuse)

        return (theta_1, theta_2, 180 - theta_3)
