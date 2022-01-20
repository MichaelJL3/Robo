
"""Kinematic types"""

from typing import Callable, TypeVar, Tuple

Config = TypeVar('Config')
Position = Tuple[float, float, float]
Kinematics = Callable[[Config, Position], Position]
