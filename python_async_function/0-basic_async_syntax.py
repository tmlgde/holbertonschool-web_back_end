#!/usr/bin/env python3
"""Module defines an asynchronous coroutine to wait for a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return delay

    Args:
        max_delay (int): maximum number of seconds to wait (default: 10)

    Returns:
        float: the random delay that was waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
