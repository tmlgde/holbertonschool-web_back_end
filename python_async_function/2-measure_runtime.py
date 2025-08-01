#!/usr/bin/env python3
"""
Module to measure the runtime of the wait_n coroutine.

This module imports the wait_n function from the previous task and
defines a measure_time function that calculates the average runtime
per execution.
"""

import asyncio
import time

# Import wait_n from the previous file (task 1)
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime of wait_n and return the average time per task.

    Args:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay for each call.

    Returns:
        float: The average time per execution of wait_n.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
