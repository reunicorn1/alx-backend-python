#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This is a function that was annorated.
    it returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
