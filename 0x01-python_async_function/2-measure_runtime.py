#!/usr/bin/env python3
"""
2. Measure the runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    --------------
    Parameters:
    n (int)
        the number of times wai_random function will be executed
    max_delay (int)
        the maximum delay to create a range for wait_random

    --------------
    Returns:
        the total_time for the execution of wait_n divided by n
    """
    start_time = time.time()

    # since 'wait_n' invovles multiple operations that could be
    # run concurrently I created a task out of it.
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    return (end_time - start_time) / n
