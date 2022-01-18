
"""Inverse kinematics through graphical analysis"""

import math

from typing import Tuple
from ..leg_config import LegConfig
from ..util.math_utils import loc_theta_degrees

def solve_inverse_kinematic(config: LegConfig, dst: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """Calculate the inverse kinematics for a graphically mapped arache leg (3DOF)

    Args:
        config (LegConfig): the leg configuration
        dst (Tuple[float, float, float]): the desired location relative to the leg base

    Returns:
        Tuple[float, float, float]: the required theta rotations to reach desired location
    """
    dst_x, dst_y, dst_z = dst

    diagonal_length = math.hypot(dst_x, dst_z)

    inner_base = diagonal_length - config.coaxia_length
    inner_hypotenuse = math.hypot(inner_base, dst_y)

    alpha_1 = math.degrees(math.acos(dst_y / inner_hypotenuse))
    alpha_2 = loc_theta_degrees(config.femur_length, inner_hypotenuse, config.tibia_length)

    theta_1 = math.degrees(math.atan2(dst_x, dst_z))
    theta_2 = alpha_1 - alpha_2
    theta_3 = loc_theta_degrees(config.femur_length, config.tibia_length, inner_hypotenuse)

    return (theta_1, theta_2, 180 - theta_3)
