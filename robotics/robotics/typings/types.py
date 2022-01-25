
"""Robotics types"""

from typing import Callable, Dict, Generator, List, TypeVar, Tuple

Servo = TypeVar('Servo')
Config = TypeVar('Config')
Vector3 = Tuple[float, float, float]
Vector2 = Tuple[float, float]
Matrix2 = List[List[float]]
Matrix3 = List[Matrix2]
PositionGenerator = Generator[Vector3, None, None]
Kinematics = Callable[[Config, Vector3], Vector3]
GeneratorFn = Callable[[], PositionGenerator]
GeneratorMap = Dict[str, GeneratorFn]
GaitProvider = Callable[[int], GeneratorFn]
