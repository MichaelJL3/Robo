
"""Math utility functions for motions"""

import math

def loc_theta(side_a: float, side_b: float, side_c: float) -> float:
    """Calculate the angle (radians) of side c using law of cosines

    Args:
        side_a (float): side of the triangle
        side_b (float): side of the triangle
        side_c (float): side of the triangle

    Returns:
        float: the angle of side c in radians
    """
    theta = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
    return math.acos(theta)

def loc_theta_degrees(side_a: float, side_b: float, side_c: float) -> float:
    """Calculate the angle (degrees) of side c using law of cosines

    Args:
        side_a (float): side of the triangle
        side_b (float): side of the triangle
        side_c (float): side of the triangle

    Returns:
        float: the angle of side c in degrees
    """
    return math.degrees(loc_theta(side_a, side_b, side_c))

def loc(side_a: float, side_b: float, theta: float) -> float:
    """Calculate the missing side c of a triangle using law of cosines

    Args:
        side_a (float): side of the triangle
        side_b (float): side of the triangle
        theta (float): angle of side c in radians

    Returns:
        float: the missing side c
    """
    c_squared = side_a**2 + side_b**2 - (2 * side_a * side_b * math.cos(theta))
    return math.sqrt(c_squared)

def loc_degrees(side_a: float, side_b: float, theta: float) -> float:
    """Calculate the missing side c of a triangle using law of cosines

    Args:
        side_a (float): side of the triangle
        side_b (float): side of the triangle
        theta (float): angle of side c in degrees

    Returns:
        float: the missing side c
    """
    return loc(side_a, side_b, math.radians(theta))

def pythagorean_side(side: float, hypotenuse: float) -> float:
    """Get the side of a triangle given one side and the hypotenuse

    Args:
        side (float): side of the triangle
        hypotenuse (float): hypotenuse of the triangle

    Returns:
        float: the missing side
    """
    return math.sqrt(hypotenuse**2 - side**2)
