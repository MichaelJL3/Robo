
"""Testing gait & kinematic scripts"""

from time import sleep

from robotics.scheduler.scheduler import Scheduler
from robotics.body.leg_3dof import Leg3DOF
from robotics.motion.frame.frame import Frame
from robotics.motion.locomotion import LocomotionController
from robotics.motion.mapping import CommonMotions
from robotics.typings.types import Vector3

from arachnid.move_iter import move_iter
from arachnid.config import get_locomotors
from arachnid.gait.gait_rotational import GaitRotational

import arachnid.kinematics.graphical_kinematics as gkinematics
import robotics.motion.kinematics.forward_frame as fkinematics

def forward_kinematics(thetas: Vector3) -> Vector3:
    #translation (90, 90, 0)
    frames = [
        Frame(rho = 66, alpha = 90, theta = 90 - thetas[0]),
        Frame(rho = 31, theta = 90 - thetas[1]),
        Frame(rho = 77, theta = -thetas[2]),
    ]

    return fkinematics.solve_forward_kinematic(frames)

def clean(tup):
    a, b, c = tup
    return (round(a, 2), round(b, 2), round(c, 2))

def fake():
    """Testing script for kinematics"""

    gait_r = GaitRotational()

    config = Leg3DOF(66.0, 31.0, 77.0)
    moves = [gait_r.__gait_provider__(i) for i in range(8)]

    for rotations in moves:
        dst = forward_kinematics(rotations)
        thetas = gkinematics.solve_inverse_kinematic(config, dst)

        print("-------")
        print(rotations)
        print(clean(dst))
        print(clean(thetas))

def translate(thetas):
    return (180 - thetas[0], thetas[1], thetas[2])

def take_step(step):
    def inner():
        print(step)

    return inner

def walk(id, theta):
    servos = []
    servos[id].angle = theta
    sleep(.33)

def main():
    move_controller = LocomotionController(get_locomotors())

    scheduler = Scheduler(1)

    walk = move_controller.start(CommonMotions.FORWARD)

    move = next(walk)
    for step in move_iter(move):
        scheduler.enqueue(take_step(step))

    scheduler.join()

if __name__ == '__main__':
    main()
