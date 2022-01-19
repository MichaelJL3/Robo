
"""Schedulder class"""

from queue import Queue
from threading import Thread
from types import FunctionType

class Scheduler(Queue):
    """Scheduler class"""

    def __init__(self, num_workers = 1, maxsize = 255):
        """constructor

        Args:
            num_workers (int, optional): The thread pool size. Defaults to 1.
            maxsize (int, optional): The maximum size of the task queue. Defaults to 255.
        """
        super().__init__(maxsize)
        self.num_workers = num_workers
        self._start_workers()

    def _start_workers(self):
        """Start the thread workpool"""
        for _ in range(self.num_workers):
            thread = Thread(target=self._worker, daemon=True)
            thread.start()

    def _worker(self):
        """Task executor"""
        while True:
            try:
                func, args, kwargs = self.get()
                func(*args, **kwargs)
            finally:
                self.task_done()

    def enqueue(self, task: FunctionType, *args, **kwargs):
        """Queue function for execution

        Args:
            task (FunctionType): the function to execute
        """
        self.put((task, args or {}, kwargs or {}))
