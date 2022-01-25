
"""Pipeline tests"""

import unittest

from robotics.pipeline import Pipeline

class TestSmoothing(unittest.TestCase):
    """Smoothing tests"""

    def test_add_function(self):
        """Test pipeline addition"""
        func_a = lambda: 5
        func_b = lambda: 5
        pipe = Pipeline()
        pipe.add(func_a)
        pipe.add(func_b)
        expected = [func_a, func_b]

        self.assertEqual(expected, pipe.funcs)

    def test_add_operator(self):
        """Test pipeline addition operator"""
        func_a = lambda: 5
        func_b = lambda: 5
        pipe = Pipeline()
        pipe += func_a
        pipe += func_b
        expected = [func_a, func_b]

        self.assertEqual(expected, pipe.funcs)

    def test_initial_pipeline(self):
        """Test pipeline addition operator"""
        func = lambda: 5
        pipe = Pipeline([func])
        expected = [func]

        self.assertEqual(expected, pipe.funcs)

    def test_merge_pipeline(self):
        """Test pipeline merge"""
        func_a = lambda: 5
        func_b = lambda: 5
        pipe_a = Pipeline([func_a])
        pipe_b = Pipeline([func_b])
        pipe_c = pipe_a.merge(pipe_b)
        expected = [func_a, func_b]

        self.assertEqual(expected, pipe_c.funcs)

    def test_call_pipeline(self):
        """Test pipeline call operator"""
        func = lambda x: x + 1
        pipe = Pipeline([func, func, func])
        expected = 3
        result = pipe(0)

        self.assertEqual(expected, result)
