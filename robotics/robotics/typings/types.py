
"""Robotics types"""

from typing import Callable, Generator, TypeVar, Tuple

Servo = TypeVar('Servo')
Config = TypeVar('Config')
Position = Tuple[float, float, float]
PositionGenerator = Generator[Position, None, None]
Kinematics = Callable[[Config, Position], Position]
