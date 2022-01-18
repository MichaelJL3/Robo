
"""Forward kinematics through graphical analysis"""

import math

from typing import Tuple
from ..leg_config import LegConfig
from ..util.math_utils import (loc_theta_degrees, loc_degrees, pythagorean_side)

class ForwardKinematicGraphicalArachneSolver:
    """Forward kinematics graphical solver for quadruped"""

    @staticmethod
    def solve(config: LegConfig, thetas: Tuple[float, float, float]) \
        -> Tuple[float, float, float]:
        """Calculate the forward kinematics for a graphically mapped arache leg (3DOF)

        Args:
            config (LegConfig): the leg configuration
            thetas (Tuple[float, float, float]): the rotations of the leg

        Returns:
            Tuple[float, float, float]: the location of the end effector relative to the base
        """
        theta_1, theta_2, theta_3 = thetas

        inner_hypotenus = loc_degrees(config.femur_length, config.tibia_length, 180 - theta_3)

        alpha_2 = loc_theta_degrees(config.femur_length, inner_hypotenus, config.tibia_length)
        alpha_1 = theta_2 + alpha_2

        p_y = math.cos(math.radians(alpha_1)) * inner_hypotenus
        diagonal_length = pythagorean_side(p_y, inner_hypotenus) + config.coaxia_length

        p_x = diagonal_length * math.sin(math.radians(theta_1))
        p_z = pythagorean_side(p_x, diagonal_length)

        return __convert_quadrant__(theta_1, p_x, p_y, p_z)

def __quadrant_conversions__(theta: float) -> Tuple[float, float, float]:
    """X/Z negative scaling on base theta

    Args:
        theta (float): the base angle

    Returns:
        Tuple[float, float, float]: the quadrant scaling
    """

    #Z/X are reversed based on current servo layout
    return (1, 1, 1) if theta <= 90 else (1, 1, -1)

def __convert_quadrant__(theta: float, p_x: float, p_y: float, p_z: float) \
    -> Tuple[float, float, float]:
    """Convert the X/Z values based on the current quadrant of the base angle

    Args:
        theta (float): the base angle
        p_x (float): the x position
        p_y (float): the y position
        p_z (float): the z position

    Returns:
        Tuple[float, float, float]: the adjusted position
    """
    x_quadrant, y_quadrant, z_quadrant = __quadrant_conversions__(theta)
    return (p_x * x_quadrant, p_y * y_quadrant, p_z * z_quadrant)
