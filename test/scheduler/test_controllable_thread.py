
"""controllable thread tests"""

import unittest

from src.scheduler.controllable_thread import ControllableThread

class TestControllableThread(unittest.TestCase):
    """controllable thread tests"""

    def test_thread_run_throws_non_implemented(self):
        """Test that the thread cannot be run directly"""
        with self.assertRaises(NotImplementedError):
            ControllableThread().run()

    def test_thread_start(self):
        """Test that the thread starts up"""
        thread = ControllableThread()
        thread.start()
        self.assertTrue(thread.is_alive())
        thread.join(timeout = 5000)
        self.assertFalse(thread.is_alive())

    def test_thread_control(self):
        """Test that the thread can pause/resume"""
        thread = ControllableThread()
        thread.resume()
        self.assertTrue(thread.event.isSet())
        thread.pause()
        self.assertFalse(thread.event.isSet())
