#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values)
    ---------------
    Parameters:
    n (int)
        the number of times wai_random function will be executed
    max_delay (int)
        the maximum delay to create a range for wait_random
    ---------------
    Returns:
        The list of the delays in ascending order
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
