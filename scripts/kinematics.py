
"""Testing gait & kinematic scripts"""

from typing import Tuple
from motion.leg_config import LegConfig
from motion.frame import Frame
from gait.gait_positional import GaitPositional
from gait.gait_rotational import GaitRotational
import motion.kinematics.forward_frame as fkinematics
import motion.kinematics.graphical_arachne as gkinematics

def forward_kinematics(thetas: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """Run the forward kinematics

    Args:
        thetas (Tuple[float, float, float]): input rotations

    Returns:
        Tuple[float, float, float]: end effector location
    """

    #translation (90, 90, 0)
    frames = [
        Frame(rho = 66, alpha = 90, theta = 90 - thetas[0]),
        Frame(rho = 31, theta = 90 - thetas[1]),
        Frame(rho = 77, theta = -thetas[2]),
    ]

    return fkinematics.solve_forward_kinematic(frames)

def clean(tup):
    a, b, c = tup
    return (round(a), round(b), round(c))

def main():
    """Testing script for kinematics"""

    gait_p = GaitPositional()
    gait_r = GaitRotational()

    config = LegConfig(66.0, 31.0, 77.0)
    moves = [gait_r.__gait_provider__(i) for i in range(8)]

    for rotations in moves:
        dst = forward_kinematics(rotations)
        thetas =  gkinematics.solve_inverse_kinematic(config, dst)

        print("-------")
        print(rotations)
        print(clean(dst))
        print(clean(thetas))

if __name__ == '__main__':
    main()
