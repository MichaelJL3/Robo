
#pylint: skip-file

"""Script for converting pwm to angle"""

import sys

def convert_pwm_to_angle(pwm: float) -> float:
    """Convert pwm to rotation angle

    Args:
        pwm (float): the pwm signal

    Returns:
        float: the rotation angle
    """
    return (pwm - 100) / 2.55

def main():
    """Main script"""

    args = sys.argv[1:]

    pwm = int(args[0])
    angle = convert_pwm_to_angle(pwm)

    print(f'{pwm} -> {angle}')

if __name__ == '__main__':
    main()
