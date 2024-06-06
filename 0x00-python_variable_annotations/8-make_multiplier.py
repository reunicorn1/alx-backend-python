#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    this function takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier.
    """
    def multiply(num: float) -> float:
        """
        This dubfunction returns the sum of the muliplication of
        multiplier with the num passed
        """
        return num * multiplier

    return multiply
