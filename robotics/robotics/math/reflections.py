
"""Reflection utilities"""

from robotics.typings.types import Vector3

def x_axis_3d(vec: Vector3) -> Vector3:
    """reflect along x axis

    Args:
        vec (Vector3): the position

    Returns:
        Vector3: the position
    """
    return (vec[0], vec[1], -vec[2])

def y_axis_3d(vec: Vector3) -> Vector3:
    """reflect along y axis

    Args:
        vec (Vector3): the position

    Returns:
        Vector3: the position
    """
    return (vec[0], -vec[1], vec[2])

def z_axis_3d(vec: Vector3) -> Vector3:
    """reflect along z axis

    Args:
        vec (Vector3): the position

    Returns:
        Vector3: the position
    """
    return (-vec[0], vec[1], vec[2])

def axis_3d(vec: Vector3, a_x = False, a_y = False, a_z = False) -> Vector3:
    """reflect along axis based on input flags

    Args:
        vec (Vector3): the position
        a_x (bool, optional): reflection flag for x. Defaults to False.
        a_y (bool, optional): reflection flag for y. Defaults to False.
        a_z (bool, optional): reflection flag for z. Defaults to False.

    Returns:
        Vector3: the position
    """
    v_x = (-vec[0]) if a_z else vec[0]
    v_y = (-vec[1]) if a_y else vec[1]
    v_z = (-vec[2]) if a_x else vec[2]
    return (v_x, v_y, v_z)

def quadrant_2_x(vec: Vector3) -> Vector3:
    """reflect x rotation into quadrant 2 relative to x

    Args:
        vec (Vector3): the rotations

    Returns:
        Vector3: the rotations
    """
    return (180-vec[0], vec[1], vec[2])

def quadrant_2_y(vec: Vector3) -> Vector3:
    """reflect y rotation into quadrant 2 relative to y

    Args:
        vec (Vector3): the rotations

    Returns:
        Vector3: the rotations
    """
    return (vec[0], 180-vec[1], vec[2])

def quadrant_2_z(vec: Vector3) -> Vector3:
    """reflect z rotation into quadrant 2 relative to z

    Args:
        vec (Vector3): the rotations

    Returns:
        Vector3: the rotations
    """
    return (vec[0], vec[1], 180-vec[2])

def quadrant_2(vec: Vector3, q_x = False, q_y = False, q_z = False) -> Vector3:
    """reflect rotations into quadrant 2 based on input flags

    Args:
        vec (Vector3): the rotations
        q_x (bool, optional): reflection flag for x. Defaults to False.
        q_y (bool, optional): reflection flag for y. Defaults to False.
        q_z (bool, optional): reflection flag for z. Defaults to False.

    Returns:
        Vector3: the rotations
    """
    v_x = (180 - vec[0]) if q_x else vec[0]
    v_y = (180 - vec[1]) if q_y else vec[1]
    v_z = (180 - vec[2]) if q_z else vec[2]
    return (v_x, v_y, v_z)
