#!/usr/bin/env python3
"""
1. Async Comprehensions
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This is a coroutine function that will collect 10 random numbers
    using an async comprehensing and return a list of 10 random
    numbers.
    ------------------
    Parameters:
    None
    ------------------
    Returns:
    a list of 10 random numbers
    """
    return [i async for i in async_generator()]
