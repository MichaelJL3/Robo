
"""scheduler tests"""

import unittest
from unittest.mock import MagicMock

from robotics.scheduler.scheduler import Scheduler

class TestScheduler(unittest.TestCase):
    """Task scheduler tests"""

    def test_queue_empty_size(self):
        """Test queue is empty"""
        scheduler = Scheduler(0)
        self.assertTrue(scheduler.empty())
        self.assertEqual(0, scheduler.qsize())

    def test_queue_not_empty_size(self):
        """Test queue is not empty"""
        mock = MagicMock()

        scheduler = Scheduler(0)
        scheduler.enqueue(mock)
        self.assertFalse(scheduler.empty())
        self.assertEqual(1, scheduler.qsize())
        self.assertFalse(mock.called)

    def test_queue_processes(self):
        """Test queue runs through"""
        mock = MagicMock()

        scheduler = Scheduler(1)
        scheduler.enqueue(mock)
        scheduler.join()
        self.assertTrue(mock.called)
