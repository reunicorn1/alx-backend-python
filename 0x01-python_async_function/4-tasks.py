#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
