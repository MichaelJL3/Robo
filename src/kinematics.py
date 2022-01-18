
"""Testing gait & kinematic scripts"""

from typing import Tuple
from gait_stages import gait
from motion.leg_config import LegConfig
from motion.frame import Frame
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
    frames = [\
        Frame(rho = 66, alpha = 90, theta = 90 - thetas[0]), \
        Frame(rho = 31, theta = 90 - thetas[1]), \
        Frame(rho = 77, theta = -thetas[2]), \
    ]

    return fkinematics.solve_forward_kinematic(frames)

if __name__ == '__main__':
    config = LegConfig(66.0, 31.0, 77.0)

    for rotations in gait():
        dst = forward_kinematics(rotations)
        thetas =  gkinematics.solve_inverse_kinematic(config, dst)

        print("-------")
        print(rotations)
        print(dst)
        print(thetas)
