
"""Controllable thread"""

from abc import abstractmethod
from threading import Thread, Event

class ControllableThread(Thread):
    """Controllable thread"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(None, args, kwargs)
        self.event = Event()
        self.pause()

    @abstractmethod
    def run(self):
        """Run the scheduler"""
        raise NotImplementedError("ControllableThread must be extended")

    def resume(self):
        """Resume the thread"""
        self.event.set()

    def pause(self):
        """Pause the thread"""
        self.event.clear()
