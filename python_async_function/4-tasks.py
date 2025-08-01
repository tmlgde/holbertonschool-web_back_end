#!/usr/bin/env python3
"""
Module that runs multiple task_wait_random concurrently
and returns a sorted list of delays.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Run task_wait_random n times and return sorted list of delays.

    Args:
        n (int): number of tasks to run
        max_delay (int): maximum delay for each task

    Returns:
        list[float]: list of delays, sorted in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # create tasks
    delays = await asyncio.gather(*tasks)  # wait for all of them
    return sorted(delays)
