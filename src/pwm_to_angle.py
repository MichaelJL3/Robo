
import sys

def convert_pwm_to_angle(pwm):
    return (pwm - 100) / 2.55

if __name__ == '__main__':
    args = sys.argv[1:]

    pwm = int(args[0])
    angle = convert_pwm_to_angle(pwm)

    print(f'{pwm} -> {angle}')

