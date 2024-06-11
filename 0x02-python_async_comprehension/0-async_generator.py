#!/usr/bin/env python3
"""
0. Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This function returns a generator that waits for 1 second,
    then yield a random number between 0 and 10.
    ----------------
    Parameters:
    None
    ----------------
    Returns:
    A generator of random numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
