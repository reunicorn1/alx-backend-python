#!/usr/bin/env python3

"""
0. The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    an asynchronous coroutine that takes an integer argument
    and waits for a random delay between the 0 and the value given
    and eventually return it
    ------------------------
    Parameters:
    max_delay :  int
        The value to be used to create a range for a random number
        to be chosen from.
    ------------------------
    Returns:
        the random delay as a float value
    """
    time: int = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
