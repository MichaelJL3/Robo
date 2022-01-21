
"""controllable thread tests"""

import unittest

from robotics.scheduler.controllable_thread import ControllableThread

class TestControllableThread(unittest.TestCase):
    """controllable thread tests"""

    def test_thread_run_throws_non_implemented(self):
        """Test that the thread cannot be run directly"""
        with self.assertRaises(NotImplementedError):
            ControllableThread().run()

    def test_thread_control(self):
        """Test that the thread can pause/resume"""
        thread = ControllableThread()
        thread.resume()
        self.assertTrue(thread.event.isSet())
        thread.pause()
        self.assertFalse(thread.event.isSet())
