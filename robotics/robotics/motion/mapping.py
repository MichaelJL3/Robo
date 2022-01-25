
"""Mapping classes"""

from enum import Enum

from robotics.body.part import Part
from robotics.typings.types import GeneratorMap, GeneratorFn

class CommonMotions(Enum):
    """Common motions enum"""
    FORWARD = 'forward'
    BACKWARD = 'backward'
    LEFT = 'left'
    RIGHT = 'right'
    TURN_LEFT = 'turn_left'
    TURN_RIGHT = 'turn_right'
    DIAG_LEFT_FORWARD = 'diag_left_forward'
    DIAG_LEFT_BACKWARD = 'diag_left_backward'
    DIAG_RIGHT_FORWARD = 'diag_right_forward'
    DIAG_RIGHT_BACKWARD = 'diag_right_backward'

class MotionMapping:
    """Motion mapping class"""

    _motion_mapping: GeneratorMap

    def __init__(self, mapping: GeneratorMap = None):
        """constructor

        Args:
            mapping (GeneratorMap, optional): the generator mapping. Defaults to None.
        """
        self._motion_mapping = mapping if mapping else {}

    def register(self, part: Part, motions: GeneratorMap):
        """Register a part with its motions

        Args:
            part (Part): the body part
            motions (GeneratorMap): generator mapping of motions
        """
        self._motion_mapping[part.name] = motions
        return self

    def get_part_mapping_by_name(self, name: str) -> GeneratorMap:
        """Get the mapping for a part

        Args:
            name (str): the part name

        Returns:
            GeneratorMap: the motion mapping
        """
        return self._motion_mapping.get(name)

    def get_part_mapping(self, part: Part) -> GeneratorMap:
        """Get the mapping for a part

        Args:
            part (Part): the body part

        Returns:
            GeneratorMap: the motion mapping
        """
        return self._motion_mapping.get(part.name)

    def get_part_motion(self, part: Part, motion: str) -> GeneratorFn:
        """Get the motion function for a part

        Args:
            part (Part): the body part
            motion (str): the motion to retrieve

        Returns:
            GeneratorFn: the motion generator
        """
        return self._motion_mapping.get(part).get(motion)

    def __setitem__(self, part: Part, mapping: GeneratorMap):
        """Set a new part mapping

        Args:
            part (Part): the body part
            mapping (GeneratorMap): the motion mapping
        """
        self.register(part, mapping)

    def __getitem__(self, part: Part) -> GeneratorMap:
        """Get the part mapping

        Args:
            part (Part): the body part

        Returns:
            GeneratorMap: the motion mapping
        """
        return self.get_part_mapping(part)

class CommonMotionsMapping(MotionMapping):
    """Common mapping motions"""

    def forward(self, part: Part) -> GeneratorFn:
        """Get the forward motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.FORWARD]

    def backward(self, part: Part) -> GeneratorFn:
        """Get the backward motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.BACKWARD]

    def left(self, part: Part) -> GeneratorFn:
        """Get the left motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.LEFT]

    def right(self, part: Part) -> GeneratorFn:
        """Get the right motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.RIGHT]

    def turn_left(self, part: Part) -> GeneratorFn:
        """Get the turn left motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.TURN_LEFT]

    def turn_right(self, part: Part) -> GeneratorFn:
        """Get the turn right motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.TURN_RIGHT]

    def diag_left_forward(self, part: Part) -> GeneratorFn:
        """Get the diagonal left forward motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.DIAG_LEFT_FORWARD]

    def diag_left_backward(self, part: Part) -> GeneratorFn:
        """Get the diagonal left backward motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.DIAG_LEFT_BACKWARD]

    def diag_right_forward(self, part: Part) -> GeneratorFn:
        """Get the diagonal right forward motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.DIAG_RIGHT_FORWARD]

    def diag_right_backward(self, part: Part) -> GeneratorFn:
        """Get the diagonal right backward motion

        Args:
            part (Part): the body part

        Returns:
            GeneratorFn: the motion generator
        """
        return self[part][CommonMotions.DIAG_RIGHT_BACKWARD]
