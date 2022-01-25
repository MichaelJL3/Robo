
"""Decorators"""

import functools

def closure(func):
    """wrap a function call to maintain original call state

    Args:
        func (Callable): the underlying function

    Returns:
        Callable: a provider function to return the function result
    """
    @functools.wraps(func)
    def wrapper_keep_args(*args, **kwargs):
        def inner():
            return func(*args, **kwargs)
        return inner
    return wrapper_keep_args
