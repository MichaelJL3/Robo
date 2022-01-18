
#from adafruit_servokit import ServoKit
#import time

from gait_stages import gait
from gait_stages import move_angles
from motion.leg_config import LegConfig
from motion.frame import Frame
from motion.kinematics.forward_frame import ForwardKinematicFrame
from motion.kinematics.forward_graphical_arachne import ForwardKinematicGraphicalArachne
from motion.kinematics.inverse_graphical_arachne import InverseKinematicGraphicalArachne

#kit = ServoKit(channels = 16)

def test_forward(thetas):
    #translation (90, 90, 0)
    frames = [\
        Frame(rho = 66, alpha = 90, theta = 90 - thetas[0]), \
        Frame(rho = 31, theta = 90 - thetas[1]), \
        Frame(rho = 77, theta = -thetas[2]), \
    ]

    return ForwardKinematicFrame.solve(frames)

def test_inverse(dst):
    config = LegConfig(66.0, 31.0, 77.0)
    return InverseKinematicGraphicalArachne.solve(config, dst)

def test_forward_old(thetas):
    config = LegConfig(66.0, 31.0, 77.0)
    return ForwardKinematicGraphicalArachne.solve(config, thetas)

if __name__ == '__main__':
    moves = move_angles(gait()) + [(0, 0, 0), (135, 0, 90)]

    for move in moves:
        pos = test_forward_old(move)
        fwd = test_forward(move)
        theta = test_inverse(fwd)

        print("-------")
        print(move)
        print(pos)
        print(fwd)
        print(theta)
        #print("-------")

    #pos = (97.0, 0.0, 0.0)

    #thetas = inverse(pos)
    #o_pos = forward(thetas)

    #print(thetas)
    #print(o_pos)

    #kit.servo[1].angle = femur
    #kit.servo[2].angle = tibia

    #time.sleep(.3)

    #kit.servo[0].angle = coaxia
