
"""Inverse kinematics through graphical analysis"""

import math

from robotics.typings.types import Vector3
from robotics.body.leg_3dof import Leg3DOF
from robotics.math.trig_utils import loc_theta_degrees, loc_degrees, pythagorean_side

def solve_inverse_kinematic(config: Leg3DOF, dst: Vector3) -> Vector3:
    """Calculate the inverse kinematics for a graphically mapped arache leg (3DOF)

    Args:
        config (Leg3DOF): the leg configuration
        dst (Vector3): the desired location relative to the leg base

    Returns:
        Vector3: the required theta rotations to reach desired location
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

    return (theta_1, theta_2, theta_3)

def solve_forward_kinematic(config: Leg3DOF, thetas: Vector3) -> Vector3:
    """Calculate the forward kinematics for a graphically mapped arache leg (3DOF)

    Args:
        config (Leg3DOF): the leg configuration
        thetas (Vector3): the rotations of the leg

    Returns:
        Vector3: the location of the end effector relative to the base
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

def __quadrant_conversions__(theta: float) -> Vector3:
    """X/Z negative scaling on base theta

    Args:
        theta (float): the base angle

    Returns:
        Vector3: the quadrant scaling
    """

    #Z/X are reversed based on current servo layout
    return (1, 1, 1) if theta <= 90 else (1, 1, -1)

def __convert_quadrant__(theta: float, p_x: float, p_y: float, p_z: float) -> Vector3:
    """Convert the X/Z values based on the current quadrant of the base angle

    Args:
        theta (float): the base angle
        p_x (float): the x position
        p_y (float): the y position
        p_z (float): the z position

    Returns:
        Vector3: the adjusted position
    """
    x_quadrant, y_quadrant, z_quadrant = __quadrant_conversions__(theta)
    return (p_x * x_quadrant, p_y * y_quadrant, p_z * z_quadrant)
