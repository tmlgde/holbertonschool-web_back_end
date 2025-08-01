#!/usr/bin/env python3

"""create task"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: Task object will execute wait_random asynchronously.
    """
    return asyncio.create_task(wait_random(max_delay))
