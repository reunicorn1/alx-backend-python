#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function measures the total runtime for async_comprehension
    which runs four times and return it.
    ------------------
    Parameters:
    None
    -----------------
    Returns:
    the total runtime
    """
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end_time = time.time()

    return end_time - start_time
