
"""Configs"""

from enum import Enum
from typing import List

from arachnid.gait.gait_positional import GaitPositional

import arachnid.kinematics.graphical_kinematics as gkinematics

from robotics.body.leg_3dof import Leg3DOF
from robotics.body.part import Part
from robotics.motion.locomotion import PartLocomotion
from robotics.motion.mapping import CommonMotions

class Legs(Enum):
    """Arachnid leg enum"""
    FL = 'fl'
    BL = 'bl'
    FR = 'fr'
    BR = 'br'

def get_locomotors() -> List[PartLocomotion]:
    """Get the locomotors

    Returns:
        List[PartLocomotion]: the locomotors
    """
    leg_config = Leg3DOF(66.0, 31.0, 77.0)
    motion_mapping = get_motion_mapping()

    legs = [Legs.FL, Legs.FR, Legs.BL, Legs.BR]

    return [PartLocomotion(
        Part(leg_config, (90, 90, 90), leg),
        motion_mapping[leg],
        gkinematics.solve_inverse_kinematic
    ) for leg in legs]

def get_motion_mapping():
    """Get the arachnid's motion mapping"""

    gait = GaitPositional()

    return {
        Legs.FR: {
            CommonMotions.FORWARD: gait.forward(4),
            CommonMotions.BACKWARD: gait.backward(2),
            CommonMotions.TURN_LEFT: gait.turn_left(0),
            CommonMotions.TURN_RIGHT: gait.turn_right(4)
        },
        Legs.BR: {
            CommonMotions.FORWARD: gait.forward(6),
            CommonMotions.BACKWARD: gait.backward(0),
            CommonMotions.TURN_LEFT: gait.turn_left(4),
            CommonMotions.TURN_RIGHT: gait.turn_right(0)
        },
        Legs.FL: {
            CommonMotions.FORWARD: gait.forward(0),
            CommonMotions.BACKWARD: gait.backward(6),
            CommonMotions.TURN_LEFT: gait.turn_left(4),
            CommonMotions.TURN_RIGHT: gait.turn_right(0)
        },
        Legs.BL: {
            CommonMotions.FORWARD: gait.forward(2),
            CommonMotions.BACKWARD: gait.backward(4),
            CommonMotions.TURN_LEFT: gait.turn_left(0),
            CommonMotions.TURN_RIGHT: gait.turn_right(4)
        }
    }
