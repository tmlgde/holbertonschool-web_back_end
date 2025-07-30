#!/usr/bin/penv python3
"""Module that defines a coroutine to run multiple wait_random concurrently."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
     """
    Spawn wait_random n times with the given max_delay and return list of delays.

    Args:
        n (int): number of times to run wait_random
        max_delay (int): maximum delay in seconds

    Returns:
        List[float]: list of delay times in ascending order
    """
    delays: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
