
"""Script for test giat"""

from gait.gait_rotational import GaitRotational
from motion.frame import Frame
from motion.leg_config import LegConfig
import motion.kinematics.forward_frame as fkinematics
import motion.kinematics.graphical_arachne as gkinematics

def translate(thetas):
    return (180 - thetas[0], thetas[1], thetas[2])

def translate_pos(pos):
    return (pos[0], pos[1], -pos[2])

def forward_kinematics(thetas):
    frames = [
        Frame(rho = 66, alpha = 90, theta = 90 - thetas[0]),
        Frame(rho = 31, theta = 90 - thetas[1]),
        Frame(rho = 77, theta = -thetas[2]),
    ]

    return fkinematics.solve_forward_kinematic(frames)

def clean(tup):
    a, b, c = tup
    return (round(a, 2), round(b, 2), round(c, 2))

def full_gait():
    gait_r = GaitRotational()

    fl = gait_r.walking_generator()
    fr = gait_r.walking_generator(2)
    bl = gait_r.walking_generator(4)
    br = gait_r.walking_generator(6)

    config = LegConfig(66.0, 31.0, 77.0)

    for _ in range(8):
        fl_thetas = next(fl)
        fr_thetas = translate(next(fr))
        bl_thetas = translate(next(bl))
        br_thetas = next(br)

        fl_pos = forward_kinematics(fl_thetas)
        fr_pos = translate_pos(forward_kinematics(fr_thetas))
        bl_pos = translate_pos(forward_kinematics(bl_thetas))
        br_pos = forward_kinematics(br_thetas)

        fl_rev_thetas = gkinematics.solve_inverse_kinematic(config, fl_pos)
        fr_rev_thetas = gkinematics.solve_inverse_kinematic(config, fr_pos)
        bl_rev_thetas = gkinematics.solve_inverse_kinematic(config, bl_pos)
        br_rev_thetas = gkinematics.solve_inverse_kinematic(config, br_pos)

        print("fl:", fl_thetas, "\tp:", clean(fl_pos), "\t0:", clean(fl_rev_thetas))
        print("fr:", fr_thetas, "\tp:", clean(fr_pos), "\t0:", clean(fr_rev_thetas))
        print("bl:", bl_thetas, "\tp:", clean(bl_pos), "\t0:", clean(bl_rev_thetas))
        print("br:", br_thetas, "\tp:", clean(br_pos), "\t0:", clean(br_rev_thetas))
        print("-----------------------")

if __name__ == '__main__':
    full_gait()
