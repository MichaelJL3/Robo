
import math
import numpy as np

from .frame import Frame

class FrameTransform(object):
    """Frame transformation functions"""

    @staticmethod
    def apply_3d(frame: Frame):
        """Create a 3d frame transform matrix

        Args:
            frame (Frame): the frame to create a transform of

        Returns:
            ndarray[float]: The 4x4 transform matrix
        """

        theta_cos = math.cos(math.radians(frame.theta))
        theta_sin = math.sin(math.radians(frame.theta))
        alpha_cos = math.cos(math.radians(frame.alpha))
        alpha_sin = math.sin(math.radians(frame.alpha))

        matrix = [
            theta_cos, -theta_sin * alpha_cos,  theta_sin * alpha_sin, frame.rho * theta_cos,
            theta_sin,  theta_cos * alpha_cos, -theta_cos * alpha_sin, frame.rho * theta_sin,
            0,          alpha_sin,              alpha_cos,             frame.delta,
            0,          0,                      0,                     1
        ]
        
        return np.array(matrix).reshape(4, 4)
