
"""Script for test giat"""

from typing import List, Tuple
from pwm_to_angle import convert_pwm_to_angle

def __move__1() -> Tuple[float, float, float]:
    """calculate the first set of rotations

    Returns:
        Tuple[float, float, float]: the rotations
    """
    pwm = 300

    theta_1 = convert_pwm_to_angle(pwm + 30)
    theta_2 = theta_3 = convert_pwm_to_angle(pwm - 200)

    return (theta_1, theta_2, theta_3)

def __move__2() -> Tuple[float, float, float]:
    """calculate the second set of rotations

    Returns:
        Tuple[float, float, float]: the rotations
    """
    pwm = 300

    theta_1 = convert_pwm_to_angle(pwm + 150)
    theta_3 = theta_2 = convert_pwm_to_angle(pwm)

    return (theta_1, theta_2, theta_3)

def __move_n__(index: int) -> Tuple[float, float, float]:
    """calculate the gait rotation based on index

    Returns:
        Tuple[float, float, float]: the rotations
    """
    if index == 0:
        return __move__1()
    if index == 1:
        return __move__2()

    pwm = 300

    theta_1 = convert_pwm_to_angle(pwm + (150 * (8-index) / 3 - 120))
    theta_3 = theta_2 = convert_pwm_to_angle(pwm)

    return (theta_1, theta_2, theta_3)

def gait() -> List[float]:
    """Get the test gait steps

    Returns:
        [float]: testing gait
    """
    return [__move_n__(i) for i in range(1, 9)]
