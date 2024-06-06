#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    This function takes a mixed list of integers and floats and
    returns the sum as floats
    """
    return float(sum(mxd_list))
