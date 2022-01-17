
import math

def loc_theta(a: float, b: float, c: float) -> float:
    """Calculate the angle (radians) of side c using law of cosines

    Args:
        a (float): side of the triangle
        b (float): side of the triangle
        c (float): side of the triangle

    Returns:
        float: the angle of side c in radians
    """
    theta = (a**2 + b**2 - c**2) / (2 * a * b)
    return math.acos(theta)

def loc_theta_degrees(a: float, b: float, c: float) -> float:
    """Calculate the angle (degrees) of side c using law of cosines

    Args:
        a (float): side of the triangle
        b (float): side of the triangle
        c (float): side of the triangle

    Returns:
        float: the angle of side c in degrees
    """
    return math.degrees(loc_theta(a, b, c))

def loc(a: float, b: float, theta: float) -> float:
    """Calculate the missing side c of a triangle using law of cosines

    Args:
        a (float): side of the triangle
        b (float): side of the triangle
        theta (float): angle of side c in radians

    Returns:
        float: the missing side c
    """
    c_2 = a**2 + b**2 - (2 * a * b * math.cos(theta))
    return math.sqrt(c_2)

def loc_degrees(a: float, b: float, theta: float) -> float:
    """Calculate the missing side c of a triangle using law of cosines

    Args:
        a (float): side of the triangle
        b (float): side of the triangle
        theta (float): angle of side c in degrees

    Returns:
        float: the missing side c
    """
    return loc(a, b, math.radians(theta))

def pythagorean_side(side: float, hypotenuse: float) -> float:
    """Get the side of a triangle given one side and the hypotenuse

    Args:
        side (float): side of the triangle
        hypotenuse (float): hypotenuse of the triangle

    Returns:
        float: the missing side
    """
    return math.sqrt(hypotenuse**2 - side**2)
