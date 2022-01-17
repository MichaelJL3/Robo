
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Frame(object):
    """DH Frame class"""

    theta: float = 0.0 # Rotation along Z axis of frame - 1
    delta: float = 0.0 # Depth distance between frame and frame - 1
    alpha: float = 0.0 # Rotation along X to line up frames Z and frame Z - 1 axis
    rho:   float = 0.0 # X distance between frame and frame - 1

    def __add__(self, o):
        """Combine two frames

        Args:
            o (Frame): frame operand

        Returns:
            Frame: the combined frame
        """
        return Frame.combine(self, o)

    @staticmethod
    def combine(a, b):
        """Combine two frames

        Args:
            a (Frame): frame operand
            b (Frame): frame operand

        Returns:
            Frame: the combined frame
        """
        return Frame(\
            theta = a.theta + b.theta,\
            delta = a.delta + b.delta,\
            alpha = a.alpha + b.alpha,\
            rho = a.rho + b.rho
        )
