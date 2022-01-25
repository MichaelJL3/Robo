
"""Decorator tests"""

import unittest

from robotics.decorators.decorators import closure

class TestDecorators(unittest.TestCase):
    """Decorator tests"""

    def test_closure(self):
        """Test function  decorator"""
        def ret_value(val: int) -> int:
            return val

        expected = 5
        provider = closure(ret_value)(expected)

        self.assertEqual(expected, provider())
        self.assertEqual(expected, provider())
