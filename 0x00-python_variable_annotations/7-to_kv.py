#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string and a number and returns a tuple
    which is the first string and the square of the int/float
    """
    return (k, v ** 2)
