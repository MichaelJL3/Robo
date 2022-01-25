
"""Reference frames"""

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Frame:
    """DH Frame class"""

    theta: float = 0.0 # Rotation along Z axis of frame - 1
    delta: float = 0.0 # Depth distance between frame and frame - 1
    alpha: float = 0.0 # Rotation along X to line up frames Z and frame Z - 1 axis
    rho:   float = 0.0 # X distance between frame and frame - 1

    def __add__(self, frame_b):
        """Combine two frames

        Args:
            frame_b (Frame): frame operand

        Returns:
            Frame: the combined frame
        """
        return Frame.combine(self, frame_b)

    @staticmethod
    def combine(frame_a, frame_b):
        """Combine two frames

        Args:
            frame_a (Frame): frame operand
            frame_b (Frame): frame operand

        Returns:
            Frame: the combined frame
        """
        return Frame(
            theta = frame_a.theta + frame_b.theta,
            delta = frame_a.delta + frame_b.delta,
            alpha = frame_a.alpha + frame_b.alpha,
            rho = frame_a.rho + frame_b.rho
        )
