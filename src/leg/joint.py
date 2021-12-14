
from __future__ import annotations
from abc import abstractmethod

class Joint(object):
    """Joint abstract class"""
    
    @property
    @abstractmethod
    def angle(self):
        """Get the angle"""
        ...

    @angle.setter
    @abstractmethod
    def angle(self, _: float):
        """Set the angle

        Args:
            _ (float): The new angle value
        """
        ...

    @property
    def next(self):
        """Get the next joint"""
        return self._next_joint

    @next.setter
    def next(self, joint: Joint):
        """Set next joint

        Args:
            joint (Joint): The next joint value
        """
        joint.prev = self
        self.next = joint

    @property
    def prev(self):
        """Get the previous joint"""
        return self._prev_joint

    @next.setter
    def prev(self, joint: Joint):
        """Set previous joint

        Args:
            joint (Joint): The previous joint value
        """
        joint.next = self
        self.prev = joint   
