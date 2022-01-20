
"""Testing gait & kinematic scripts"""

from sched import scheduler
import sched
from typing import Tuple
from motion.leg_state import LegState

from scheduler.move_controller import MoveController
from scheduler.scheduler import Scheduler
from gait.gait_positional import GaitPositional
from gait.gait_rotational import GaitRotational
from motion.leg_config import LegConfig
from motion.frame import Frame

import motion.kinematics.forward_frame as fkinematics
import motion.kinematics.graphical_arachne as gkinematics

Position = Tuple[float, float, float]

def forward_kinematics(thetas: Position) -> Position:
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

    gait_p = GaitPositional()
    gait_r = GaitRotational()

    config = LegConfig(66.0, 31.0, 77.0)
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

def main():
    #thetas_f_r = translate(gkinematics.solve_inverse_kinematic(config, next(f_r)))
    #thetas_b_r = translate(gkinematics.solve_inverse_kinematic(config, next(b_r)))

    leg_config = LegConfig(66.0, 31.0, 77.0)

    legs = [
        LegState(leg_config, (90, 90, 90), walking_id=0, turning_id=0),
        LegState(leg_config, (90, 90, 90), walking_id=2, turning_id=4),
        LegState(leg_config, (90, 90, 90), walking_id=4, turning_id=4),
        LegState(leg_config, (90, 90, 90), walking_id=6, turning_id=0)
    ]

    move_controller = MoveController(GaitPositional(), legs)
    scheduler = Scheduler(1)

    walk = move_controller.walking()

    for step in MoveController.rotation_iter(next(walk)):
        scheduler.enqueue(take_step(step))

    scheduler.join()

if __name__ == '__main__':
    main()
