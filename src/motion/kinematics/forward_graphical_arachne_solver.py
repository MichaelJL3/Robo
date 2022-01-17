
import math

from typing import Tuple
from ..leg_config import LegConfig
from ..util.math_utils import (loc_theta_degrees, loc_degrees, pythagorean_side)

class ForwardKinematicGraphicalArachneSolver:
    """Forward kinematics graphical solver for quadruped"""

    @staticmethod
    def solve(config: LegConfig, thetas: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """Calculate the forward kinematics for a graphically mapped arache leg (3DOF)

        Args:
            config (LegConfig): the leg configuration
            thetas (Tuple[float, float, float]): the rotations of the leg

        Returns:
            Tuple[float, float, float]: the location of the end effector relative to the base
        """

        coaxia_length = config.coaxia_length
        femur_length  = config.femur_length
        tibia_length  = config.tibia_length

        theta_1, theta_2, theta_3 = thetas

        inner_hypotenus = loc_degrees(femur_length, tibia_length, 180 - theta_3)

        alpha_2 = loc_theta_degrees(femur_length, inner_hypotenus, tibia_length)
        alpha_1 = theta_2 + alpha_2

        y = math.cos(math.radians(alpha_1)) * inner_hypotenus
        diagonal_length = pythagorean_side(y, inner_hypotenus) + coaxia_length

        x = diagonal_length * math.sin(math.radians(theta_1))
        z = pythagorean_side(x, diagonal_length)

        return __convert_quadrant__(theta_1, x, y, z)

def __quadrant_conversions__(theta: float) -> Tuple[float, float, float]:
    """X/Z negative scaling on base theta

    Args:
        theta (float): the base angle

    Returns:
        Tuple[float, float, float]: the quadrant scaling
    """

    if theta <= 90:
        return (1, 1, 1)
    elif theta <= 180:
        #Z/X are reversed based on current servo layout
        return (1, 1, -1)

def __convert_quadrant__(theta: float, x: float, y: float, z: float) -> Tuple[float, float, float]:
    """Convert the X/Z values based on the current quadrant of the base angle

    Args:
        theta (float): the base angle
        x (float): the x position
        y (float): the y position
        z (float): the z position

    Returns:
        Tuple[float, float, float]: the adjusted position
    """

    x_quadrant, y_quadrant, z_quadrant = __quadrant_conversions__(theta)
    return (x * x_quadrant, y * y_quadrant, z * z_quadrant)
