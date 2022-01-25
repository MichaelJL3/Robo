
"""Pipeline class"""

from __future__ import annotations
from functools import reduce
from typing import Callable, List, TypeVar

TIn = TypeVar("TIn")
TOut = TypeVar("TOut")
PipeFunction = Callable[[TIn], TOut]

class Pipeline:
    """Pipeline class"""

    _funcs: List[PipeFunction] = []

    def __init__(self, funcs: List[PipeFunction] = None):
        """constructor

        Args:
            funcs (List[PipeFunction], optional): list of functions to chain. Defaults to None.
        """
        self._funcs = funcs if funcs is not None else []

    @property
    def funcs(self) -> List[PipeFunction]:
        """Get the list of functions

        Returns:
            List[PipeFunction]: the list of functions
        """
        return self._funcs

    def __add__(self, item: PipeFunction):
        """Add a function to the chain

        Args:
            item (PipeFunction): the function to add
        """
        return self.add(item)

    def add(self, item: PipeFunction) -> Pipeline:
        """Add a function to the chain

        Args:
            item (PipeFunction): the function to add

        Returns:
            Pipeline: the pipeline
        """
        self._funcs.append(item)
        return self

    def merge(self, pipe: Pipeline) -> Pipeline:
        """Merge two pipelines

        Args:
            pipe (Pipeline): the appending pipeline

        Returns:
            Pipeline: the merged pipeline
        """
        return Pipeline(self._funcs + pipe.funcs)

    def __call__(self, args: TIn) -> TOut:
        """Activate the pipeline

        Args:
            args (TIn): input arg to the pipeline

        Returns:
            TOut: pipeline output
        """
        return reduce(lambda data, func: func(data), self._funcs, args)
